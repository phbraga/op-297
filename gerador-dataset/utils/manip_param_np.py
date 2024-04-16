def manip_param_np(TagAnt, ac, crmp):
    # ENTRADA DOS DADOS SALVOS NO VETOR AC DE STRINGS
    # SEGUNDA ETAPA PARA GERAS AS TAGS PRO .DAT
    npp = crmp["num_prod"]  # numero de pocos produtores
    npi = crmp["num_inj"]  # numero de pocos injetores
    ncc = crmp["control_steps"]  # numero de ciclos de controle
    mqp = crmp["q_prod"][1]
    mqi = crmp["q_inj"][1]

    tags = []

    for it in range(ncc):
        for ip in range(npp):
            ivarp = ip + (npp + npi) * it
            if crmp["var_tipo"][0] == 1:  # ---> vazao produtores (absoluta)
                vazao_absoluta = TagAnt[ivarp]["val"] * mqp
            else:  # ---> BHP produtores
                vazao_absoluta = (
                    1
                    + (
                        (crmp["bhp_prod"][1] - crmp["bhp_prod"][0])
                        / crmp["bhp_prod"][0]
                    )
                    * (TagAnt[ivarp]["val"])
                ) * (crmp["bhp_prod"][0])
            tags.append(
                {"name": "$GP{}_{}".format(it + 1, ip + 1), "val": vazao_absoluta}
            )
        
        injector_params(TagAnt, crmp, npp, npi, tags, it)
        if crmp["wag"]:
            injector_params(TagAnt, crmp, npp, npi, tags, it)

    return tags

def injector_params(TagAnt, crmp, npp, npi, tags, it):
    for ip in range(npi):
        ivari = ip + (npp + npi) * it + npp
        if crmp["var_tipo"][1] == 1:  # ---> vazao injetores (absoluta)
            vazao_absoluta = (
                    1
                    + ((crmp["q_inj"][1] - crmp["q_inj"][0]) / crmp["q_inj"][0])
                    * (TagAnt[ivari]["val"])
                ) * crmp["q_inj"][
                    0
                ]  # Checar !!
        else:  # ---> BHP injetores
            vazao_absoluta = (
                    1
                    + ((crmp["bhp_inj"][1] - crmp["bhp_inj"][0]) / crmp["bhp_inj"][0])
                    * (TagAnt[ivari]["val"])
                ) * crmp["bhp_inj"][
                    0
                ]  # Checar !!
        tags.append(
                {"name": "$GI{}_{}".format(it + 1, ip + 1), "val": vazao_absoluta}
            )
