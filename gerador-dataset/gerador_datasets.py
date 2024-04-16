## DADOS DO C�DIGO --------------------------------------------------------
# UNIVERSIDADE FEDERAL DE PERNAMBUCO - UFPE
# CENTRO DE TECNOLOGIA E GEOCIENCIAS - CTG
# PROGRAMA DE POS-GRADUACAO EN ENGENHARIA CIVIL
# TYPE OF FILE: MAIN
# ADVISOR: BERNARDO HOROWITZ
# PROGRAMMERS FOR BUGGES AND EGG - PROGRAMER: JUAN ALBERTO ROJAS TUEROS - TANSLATOR: MATEUS GONCALVES MACHADO
# PROGRAMMER FOR WAG: PEDRO HENRIQUE MAGALHÃES BRAGA


import numpy as np

from generator import generate_data
from utils import (
    filter_report,
    get_params,
    ponto_inicial,
    tpl_generator,
)


def main(args):
    """
    Funcao principal do gerador de dataset
    args: dict -> Dicionario com os argumentos de entrada
    """
    # Adicionar documentacao
    init_counter = args.init_counter
    num_amostras = args.num_amostras
    reports = []
    # Se o contador for diferente de 0, carrega o dataset anterior e faz stack com novo .npy diferente do carregado
    crmp = get_params(dataset=args.dataset)
    if crmp["generate_tpl"]:
        tpl_generator(crmp)
    for cont in range(init_counter, init_counter + num_amostras):
        ## DEFINI��O DO PONTO DE PARTIDA | PONTO INICIAL PARA A SIMULA��O
        crmp["x0"] = ponto_inicial(crmp)

        if "wag" in crmp.keys() and crmp["wag"]:
            crmp["x1"] = crmp["x0"].copy()
            crmp["x2"] = ponto_inicial(crmp)
            crmp["x0"] = np.empty_like(crmp["x2"])
            
            control_wag_changes = 1
            control_wag_x1 = 0
            control_wag_x2 = 0
            curr_wag_inj = 1
            wag_inj = crmp["x1"]
            wag_inj_i = 0
            step = (crmp["num_prod"] + crmp["num_inj"]) * 8
            for i in range(len(crmp["x0"])):
                crmp["x0"][i] = wag_inj[wag_inj_i]
                wag_inj_i += 1

                if control_wag_changes > step:
                    if curr_wag_inj == 1:
                        control_wag_x1 = wag_inj_i
                        wag_inj_i = control_wag_x2
                        wag_inj = crmp["x2"]
                    else:
                        control_wag_x2 = wag_inj_i
                        wag_inj_i = control_wag_x1
                        wag_inj = crmp["x1"]
            
                control_wag_changes += 1
        
        R = generate_data(crmp, cont)
        reports.append(filter_report(R, crmp))

    dataset_name = crmp["ac1"].split("/")[1].split("_")[0]
    reports.sort(key=lambda x: x.shape[0])
    reshaped_reports = np.stack(
        [reports[0]] + [report[: reports[0].shape[0], :] for report in reports[1:]]
    )
    np.save("Data/" + dataset_name + ".npy", reshaped_reports)


# Fazer gerador de template

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", help="Dataset a ser criado", default="WAG")
    parser.add_argument(
        "--num-amostras", help="Numero de amostras a serem geradas", type=int, default=1
    )
    parser.add_argument(
        "--init-counter",
        help="Numero de amostras ja geradas (Ponto de partida para a geracao atual)",
        type=int,
        default=0,
    )
    args = parser.parse_args()
    main(args)
