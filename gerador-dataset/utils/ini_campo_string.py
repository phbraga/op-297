def ini_campo_string(crmp):
    # NÚMERO DE POCOS PRODUTORES
    # ac(3) - npp - Número de pocos produtores
    crmp["ac3"] = str(crmp["num_prod"])

    # NÚMERO DE POCOS INJETORES
    # ac(4) - npi - Número de pocos injetores
    crmp["ac4"] = str(crmp["num_inj"])

    # NÚMERO DE CICLOS DE CONTROLE UTILIZADO (STEP CONTROL)
    # ncc - Número de ciclos de controle (UNIDADE: DIAS)
    crmp["ac5"] = str(crmp["control_steps"])

    # TEMPO DE CONCESSÃO DO RESERVATÓRIO | TEMPO DE PRODUÇÃO TOTAL
    # ac(6) - Tc - Tempo de concessão (UNIDADE: ANOS)
    crmp["ac6"] = str(crmp["t_concessao"])

    ret_code = 0  # Saída normal !!!! O QUE SIGNIFICA !!!

    return ret_code
