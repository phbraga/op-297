import os


def process_rwd(template_file, output_file):
    """
    Copy results report template file to output file, substituting the names of files.
    template_file: (string) name of input template file.
    output_file: (string) name of processed output file.
    """

    try:
        inpf = open(template_file, "rt")
    except IOError as e:
        print("Error opening file {}: {}".format(template_file, e))
        raise

    try:
        outf = open(output_file, "wb")
    except IOError as e:
        print("Error opening file {}: {}".format(output_file, e))
        raise

    x = "<file>"
    imex_base_name, _ = os.path.splitext(output_file)
    imex_base_name = imex_base_name.split(os.sep)[-1]
    y = imex_base_name

    line = inpf.readline()
    line = line.replace(x, y)
    outf.write(line.encode())

    while True:
        line = inpf.readline()
        outf.write(line.encode())
        if not line:
            break

    inpf.close()
    outf.close()
