import os

from utils.clean_up import clean_up
from utils.make_file_name import make_file_name
from utils.manip_param_np import manip_param_np
from utils.pos_processador_crm import pos_processador_crm
from utils.process_files_ncte import process_files_ncte
from utils.process_rwd import process_rwd
from utils.read_param import read_param


def generate_data(crmp, cont, tag_data="x0"):
    """
    generate_data:
    Generator function that executes various steps for CRMP analysis.
    crmp: (structure) CRMP parameters.
    cont: (integer) counter step.

    Returns:
    R: (array) processed data after running IMEX.
    """

    # Read parameters and generate tags for IMEX .dat file
    TagMod, ac = read_param(crmp, crmp[tag_data])
    tags = manip_param_np(TagMod, crmp)

    return write_outputs(tags, crmp, ac, cont)


def write_outputs(tags, crmp, ac, cont):
    templateFileName = ac[0]
    runDir = ac[1]
    templaterwd = ac[-1]

    # Create runDir folder and the necessary files for IMEX
    imexFile = make_file_name(runDir, crmp["dataset"], cont)

    # Copy the template file (.tpl) to imexFile.Input (.dat), replacing the variables indicated in tags
    process_files_ncte(
        templateFileName, os.path.join(runDir, imexFile["Input"]), tags, "\$"
    )

    # Populate the .rwd file used by results_report
    process_rwd(templaterwd, os.path.join(runDir, imexFile["rwd"]))
    
    if crmp["run_simulator"]:
        # Run IMEX.exe
        imexCmd = f"{crmp['executa_imex']} {os.path.join(runDir, imexFile['Input'])} -log -jacpar -parasol {crmp['par_imex']} -wait"
        status = os.system(imexCmd)
        print(imexCmd)
        if status != 0:
            print("Error running imex!")
            raise Exception("Problem running IMEX.")

        # Run REPORT.exe
        reportCmd = f"{crmp['executa_report']} {os.path.join(runDir, imexFile['rwd'])} -o {os.path.join(runDir, imexFile['rwo'])}"
        status = os.system(reportCmd)
        if status != 0:
            print("Error running report!")
            raise Exception("Problem running report.")

        # Process output data after running IMEX with defined tags
        report = pos_processador_crm(crmp, os.path.join(runDir, imexFile["rwo"]))

        # Cleanup files
        clean_up(runDir, imexFile, crmp)

        return report
