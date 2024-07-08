import json

def verifica_comando(texto:str):
    texto = texto.lower()
    if texto == 'sair' or texto == 's':
        return True
    
    elif texto == 'listar':
        listar(lista_tarefaz)
    elif texto == 'desfazer':
        desfazer(lista_tarefaz)
    elif texto == 'refazer':
        refazer(lista_desfazer)
    else:
        lista_tarefaz.append(texto)
        listar(lista_tarefaz)

def listar(lista_tarefaz): 
    if not lista_tarefaz:
        print('Não possui tarefaz')
        return None
    
    print('Tarefaz:')
    for tarefa in lista_tarefaz:
            print(tarefa)
        
    
    print()

def desfazer(lista_tarefaz):
    if lista_tarefaz:
        removido = lista_tarefaz.pop()
        lista_desfazer.append(removido)
    else:
        print('Não possui tarefaz para remover')
        
    listar(lista_tarefaz)
    
def refazer(lista_removida):
    if lista_removida:
        refazer  = lista_removida.pop()
        lista_tarefaz.append(refazer)
    else:
        print('Não possui tarefaz para refazer')
        
    listar(lista_tarefaz)

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquvio não encontrado')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'aula192.json'
lista_tarefaz = ler([], CAMINHO_ARQUIVO)
lista_desfazer = []
     
while True:
    print('Comandos: listar, desfazer, refazer')
    entrada = str(input('Digite uma tarefa ou comando: '))
    print()
    confirmacao = verifica_comando(entrada)
    salvar(lista_tarefaz, CAMINHO_ARQUIVO)
    if confirmacao:
        break
    