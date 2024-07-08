import os

lista_compras = []

while True:
    print('Selecione uma opção')
    escolha = input('[i]nserir [a]pagar [l]istar: ')

    if escolha == 'i' or escolha == 'I':
        os.system('cls')
        item = input('Valor: ')
        lista_compras.append(item)
    
    elif escolha == 'a' or escolha == 'A':
        os.system('cls')
        indice = input('informe o indice que deseja apagar: ')
        try:
            apagado = lista_compras.pop(int(indice))
            print(f'O item {apagado} foi apagado da lista de compras')
        except ValueError:
            print('por favor digite um número int')

        except IndexError:
            print('Indice não existe')

    elif escolha == 'l' or escolha == 'I':
        os.system('cls')
        for indice, valor in enumerate(lista_compras):
            print(indice, valor)
    
    else:
        print('Por favor escolha entre "i" "a" ou "l"')