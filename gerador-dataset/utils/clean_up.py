import os


def clean_up(run_dir, imex_file, crmp):
    """
    clean_up:
    Removes specific files after each run.
    run_dir: (string) directory path.
    imex_file: (dictionary) IMEX file names.
    crmp: (structure) CRMP parameters.
    """

    if crmp["delsim"] == 1:
        os.remove(imex_file["Log"])
        os.remove(imex_file["Output"])
        os.remove(imex_file["Index"])

        # Clean up after every run
        # os.remove(imex_file['Input'])
        # os.remove(imex_file["Results"])
        os.remove(os.path.join(run_dir, imex_file["rwd"]))
        os.remove(os.path.join(run_dir, imex_file["rwo"]))
        # os.remove(imex_file["rstrsr3"])
        # os.remove(imex_file["rstrmrf"])
