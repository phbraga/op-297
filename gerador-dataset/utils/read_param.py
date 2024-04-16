def read_param(crmp, var):
    # readDakotaParam:
    # create a table of pairs (name, value)
    # from a dakota parameter file
    # tags: (array of structures) array of (name, value) pairs.
    # var: design variable

    nvar = len(var)
    tags = []

    for ivar in range(nvar):
        tags.append({"val": var[ivar]})

    # GERA UM VETOR TIPO STRING COM OS DADOS DE ENTRADAS VINDAS DO CRMP
    ac = [crmp["ac1"], crmp["ac2"], crmp["ac3"], crmp["ac4"], crmp["ac5"], crmp["ac7"]]

    # SAIDAS: TAGS E O VETOR AC
    return tags, ac
