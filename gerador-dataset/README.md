# Gerador de datasets para Projeto OP297

Passo a passo:

- Coloque seu template na pasta de template
    - O gerador tem a opção do template ter ou não os controles definidos
    - Caso os controles não sejam definidos, será gerado um template novo

- Configure seu dataset a ser gerado em configs.yml
    - Cada parâmetro de configuração está descrito na seção de [Configurações](#Configurações)

- [Rode o código](#rodando-codigo)

    - O parâmetro "dataset" é o mesmo nome do dataset posto na pasta configs

    - O parâmetro "num-amostras" define quantas amostras você quer que sejam geradas

    - O parâmetro "init-counter" é o número da amostra de ponto de partida à ser gerada. Caso ela seja diferente de 0, o gerador irá carregar um dataset pré-gerado e que estará na pasta "Data"

- O dataset gerado estará na pasta "Data"

## Rodando o Código
```shell
python gerador_datasets.py --dataset NOME_DATASET --num-amostras QTDE_AMOSTRAS_PARA_GERAR --init-counter PONTO_DE_PARTIDA  
```

## Configurações

- Wcontrols: int -> Tipo de controle (1 - Controles Correlacionados, 2 - Controles Aleatorios)
- var_tipo: list -> Tipo de variavel [prod, inj] (1 - Vazao, 2 - BHP)
- simulador: int -> Executar o simulador ou nao (1 - Sim, 2 - Nao)
- delsim: int -> Deletar os arquivos do simulador ou nao (1 - Sim, 2 - Nao)
- par_imex: int -> Numero de processadores para executar o IMEX
- t_concessao: int -> Tempo de concessao da producao do reservatorio
- num_prod: int -> Numero de pocos produtores
- num_inj: int -> Numero de pocos injetores
- control_steps: int -> Numero de ciclos de controle
- delta1: float -> Tamanho de perturbacao para o produtor
- delta2: float -> Tamanho de perturbacao para o injetor
- temporal: int -> Tamanho de correlacao temporal entre ciclos de controle
- ac1: str -> Arquivo template com as informacoes do reservatorio
- ac7: str -> Arquivo template com as informacoes de saida no arquivo report
- ac2: str -> Pasta onde serao escritos os arquivos do IMEX
- window_size: int -> Tamanho da janela de amostragem
- tpl_time_skip: int -> Numero de passos de tempo a serem pulados inicialmente no template
- sim_time: int -> Tempo de simulacao
- generate_tpl: bool -> Gerar novo arquivo .tpl ou nao
- executa_imex: str -> Comando para executar o IMEX
- executa_report: str -> Comando para executar o REPORT