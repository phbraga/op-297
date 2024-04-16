import os


def make_file_name(runDir, dataset, cont):
    # make_file_name: create imex files names for
    # running imex in runDir directory
    # runDir: (string) execution directory

    if not os.path.isdir(runDir):
        try:
            os.mkdir(runDir)
        except OSError as e:
            print(f"Error making directory {runDir}.")
            print(f"Error message is: {e}.")

    imexBaseName = f"{dataset}DataSetBHP_Rate_correlation{cont}"

    imexFile = {}
    imexFile["Input"] = f"{imexBaseName}.dat"
    imexFile["Output"] = f"{imexBaseName}.out"
    # imexFile["Results"] = f"{imexBaseName}.mrf"
    imexFile["Index"] = f"{imexBaseName}.sr3"
    imexFile["Log"] = f"{imexBaseName}.log"
    imexFile["rwd"] = f"{imexBaseName}.rwd"  # novo!
    imexFile["rwo"] = f"{imexBaseName}.rwo"  #
    # imexFile["rstrsr3"] = f"{imexBaseName}.rstr.sr3"  # novo
    # imexFile["rstrmrf"] = f"{imexBaseName}.rstr.mrf"  # novo

    return imexFile
