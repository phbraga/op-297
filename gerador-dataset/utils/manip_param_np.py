def manip_param_np(TagAnt, crmp):
    # ENTRADA DOS DADOS SALVOS NO VETOR AC DE STRINGS
    # SEGUNDA ETAPA PARA GERAS AS TAGS PRO .DAT
    npp = crmp["num_prod"]  # numero de pocos produtores
    npi = crmp["num_inj"]  # numero de pocos injetores
    ncc = crmp["control_steps"]  # numero de ciclos de controle

    tags = []
    curr_steps = 1
    is_wag = "wag" in crmp.keys() and crmp["wag"] and "npw" in crmp.keys()
    tag_norm = "_wag" if is_wag else ""

    for it in range(ncc):
        producer_params(TagAnt, crmp, npp, npi, tags, it)
        injector_params(TagAnt, crmp, npp, npi, tags, it, tag_norm=tag_norm)

        curr_steps += 1
        if is_wag and curr_steps > crmp["npw"]:
            curr_steps = 1
            tag_norm = "" if "_wag" in tag_norm else "_wag"

    return tags

def producer_params(TagAnt, crmp, npp, npi, tags, it):
    for ip in range(npp):
        ivarp = ip + (npp + npi) * it
        if crmp["var_tipo"][0] == 1:  # ---> vazao produtores (absoluta)
            vazao_absoluta = TagAnt[ivarp]["val"] * crmp[f"q_prod"][1]
        else:  # ---> BHP produtores
            vazao_absoluta = (
                    1
                    + (
                        (crmp[f"bhp_prod"][1] - crmp[f"bhp_prod"][0])
                        / crmp[f"bhp_prod"][0]
                    )
                    * (TagAnt[ivarp]["val"])
                ) * (crmp[f"bhp_prod"][0])
        tags.append(
                {"name": "$GP{}_{}".format(it + 1, ip + 1), "val": vazao_absoluta}
            )

def injector_params(TagAnt, crmp, npp, npi, tags, it, tag_norm=""):
    for ip in range(npi):
        ivari = ip + (npp + npi) * it + npp
        if crmp["var_tipo"][1] == 1:  # ---> vazao injetores (absoluta)
            vazao_absoluta = (
                    1
                    + ((crmp[f"q_inj{tag_norm}"][1] - crmp[f"q_inj{tag_norm}"][0]) / crmp[f"q_inj{tag_norm}"][0])
                    * (TagAnt[ivari]["val"])
                ) * crmp[f"q_inj{tag_norm}"][
                    0
                ]  # Checar !!
        else:  # ---> BHP injetores
            vazao_absoluta = (
                    1
                    + ((crmp[f"bhp_inj{tag_norm}"][1] - crmp[f"bhp_inj{tag_norm}"][0]) / crmp[f"bhp_inj{tag_norm}"][0])
                    * (TagAnt[ivari]["val"])
                ) * crmp[f"bhp_inj{tag_norm}"][
                    0
                ]  # Checar !!
        tags.append(
                {"name": "$GI{}_{}".format(it + 1, ip + 1), "val": vazao_absoluta}
            )
