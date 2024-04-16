import re


def process_files_ncte(template_file, output_file, tags, marker):
    """
    Copy template file to output file, substituting the variables indicated
    in the tags array by their corresponding values.
    template_file: (string) name of input template file.
    output_file: (string) name of processed output file.
    tags: (array of structures) name/value pairs.
    marker: (string) delimiter for variable
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

    file_contents = inpf.read()

    # Create a pattern to define a variable.
    # Starts with the marker, followed by one or more word characters,
    # and ends with a non-word character.
    var_pattern = r"{}{}".format(marker, r"\w+")

    # Find out where all variables start and end.
    vstart = []
    vend = []
    vname = []
    for match in re.finditer(var_pattern, file_contents):
        vstart.append(match.start())
        vend.append(match.end())
        vname.append(match.group())

    # Write output file, replacing the variables by their values.
    seg_start = 0
    for ivar in range(len(vstart)):
        outf.write(file_contents[seg_start : vstart[ivar]].encode())
        for jvar in range(len(tags)):
            if tags[jvar]["name"] == vname[ivar]:
                out_str = str(tags[jvar]["val"])[1:-1]
                inteira = out_str.split(".")[0]
                decimal = out_str.split(".")[1]
                decimal = decimal[:2]
                out_str = inteira + "." + decimal
                outf.write(out_str.encode())
        seg_start = vend[ivar]

    # Last segment
    outf.write(file_contents[seg_start:].encode())

    inpf.close()
    outf.close()
