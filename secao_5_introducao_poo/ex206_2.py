import json
from ex206_1 import Pessoa, CAMINHO_ARQUIVO

def ler(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquvio não encontrado')
    return dados
dados =[]
dados = ler(CAMINHO_ARQUIVO)
dadodsad = [1,2,3]

print(len(dados))
for pessoa in range(len(dados)):
    print(dados[pessoa])  
mateus = Pessoa(**dados[0])
fernada = Pessoa(**dados[1])
jose = Pessoa(**dados[2])

print(mateus.get_nome())