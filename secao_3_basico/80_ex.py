# Exercício - sistema de perguntas e respostas
import random

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
numero_aleatorio = random.randint(0,2)

print(perguntas[numero_aleatorio]['Pergunta'])
print(f'Opções: {perguntas[numero_aleatorio]['Opções']}')
resposta_correta = int(perguntas[numero_aleatorio]['Resposta'])
while True:
    try:
        resposta_user = int(input('Informe a resposta correta: '))
        if resposta_user == resposta_correta:
            print('Resposta correta')
            break
        elif resposta_user != resposta_correta:
            print('Resposta incorreta!')
            print(f'A resposta era {resposta_correta}')
            break
    except ValueError:
        print('Informe um número inteiro')