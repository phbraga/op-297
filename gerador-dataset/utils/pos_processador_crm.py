import numpy as np


def transform_report(report):
    report[:, 0] = report[:, 0].astype(int)
    unique_values = np.unique(report[:, 0])
    filtered_array = np.array([])
    for value in unique_values:
        # Find the last row in the array with the current value in the first column.
        # print(np.where(report[:, 0] == value))
        last_row_index = np.where(report[:, 0] == value)[-1][0]
        # # Add the last row to the filtered array.
        filtered_array = np.append(filtered_array, report[last_row_index, :], axis=0)
    report = filtered_array.reshape((len(unique_values), report.shape[1]))
    return report


def pos_processador_crm(crmp, sim_output_file):
    """
    pos_processador_crm:
    Reads the .RWO file and imports the data into a matrix.
    crmp: (structure) CRMP parameters.
    sim_output_file: (string) name of the simulation output file.
    Returns the data matrix.
    """

    try:
        fid = open(sim_output_file, "rt")
    except IOError as e:
        print("Error opening file {}: {}".format(sim_output_file, e))
        raise

    # Eliminating the first lines of the report file.
    for _ in range(9):
        fid.readline()

    # Importing the data into a matrix.
    col = 4 * crmp["num_prod"] + 2 * crmp["num_inj"] + 1
    fid_read = np.loadtxt(fid, dtype=float)
    R = fid_read.reshape((-1, col))
    # Close the file.
    fid.close()

    return transform_report(R)
