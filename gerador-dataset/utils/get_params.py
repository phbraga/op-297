from yaml import load
from yaml.loader import SafeLoader

from utils import ini_campo_string


def get_params(dataset):
    """
    Funcao que retorna um dicionario com os parametros de entrada para o template
    """

    with open(f"configs/{dataset}.yml", "r") as f:
        crmp = load(f, Loader=SafeLoader)

    crmp["dataset"] = dataset
    if ini_campo_string(crmp):
        print("Erro na inicializa��o do campo string")
        exit()

    return crmp
