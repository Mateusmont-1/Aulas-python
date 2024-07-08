frase = 'O python é uma linguagem de programação ' \
    'multiparadigma.' \
    'Python foi criado por Guido van Rossumaaaaaaaaa.'

i = 0
apareceu_mais_vezes = 0
letra_mais_apareceu = ''
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue

    if quantas_vezes_letra_apareceu > apareceu_mais_vezes:
        apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_mais_apareceu = letra_atual
    
    i += 1

print(f'A letra que mais apareceu foi "{letra_mais_apareceu}" e apareceu {apareceu_mais_vezes} vezes')