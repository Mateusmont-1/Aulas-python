import os

palavra = 'perfume'
letras_acertadas = ''
tentativas = 0
while True:

    letra_digitada = input('Digite uma letra: ')
    tamanho = len(letra_digitada)
    if tamanho > 1:
        print('Digite apenas uma letra')
        continue

    
    if letra_digitada in palavra:
        letras_acertadas +=letra_digitada
    palavra_formada = ''
    for letra_secrata in palavra:
        if letra_secrata in letras_acertadas:
            palavra_formada += letra_secrata
        else:
            palavra_formada += '*'
    print('Palavra formada', palavra_formada)
    tentativas +=1
    if palavra_formada == palavra:
        os.system('cls')
        print('Palavra formada', palavra_formada)
        print('Parabens você acertou')
        print('Tentativas:', tentativas)
        letras_acertadas = ''
        tentativas = 0
        