import json

class Pessoa:
    
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def get_sexo(self):
        return self.sexo
    
def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'headers.json'

    # Define os cabeçalhos da requisição
headers = {
	"X-RapidAPI-Key": "06f0c1d958mshcd70f7d1495b050p1b4cb5jsnd9f5e358c544",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
salvar(headers, CAMINHO_ARQUIVO)
# mateus = Pessoa('Mateus', 23, 'Masculino')
# fernanda = Pessoa('Fernanda', 25, 'Feminina')
# Jose = Pessoa('Jose', 22, 'Masculino')
# bd = [vars(mateus), vars(fernanda), vars(Jose)]

# print(mateus.get_nome())
# salvar(bd, CAMINHO_ARQUIVO)
# salvar(bd, CAMINHO_ARQUIVO)
