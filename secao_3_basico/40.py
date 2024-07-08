while True:
    try:
        numero_1 = input('Digite um número: ')
        numero_2 = input('Digite outro número: ')
        operador = input('Digite o operador (+-/*): ')
        operador_str = ''
        conta = 0.0
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
    except:
        print('Valores digitados incorretamente')
        continue


    if operador == '+':
        conta = numero_1_float + numero_2_float
        operador_str = 'soma'
    
    elif operador == '-':
        conta = numero_1_float - numero_2_float
        operador_str = 'subtração'
    
    elif operador == '/':
        conta = numero_1_float / numero_2_float
        operador_str = 'divisão'
    
    elif operador == '*':
        conta = numero_1_float * numero_2_float
        operador_str = 'multiplicação'

    else:
        print('Operador informado não existente')
        print('Repita a operação novamente')
        continue

    print(f'A {operador_str} entre {numero_1} e {numero_2} é igual a {conta}')
    sair = input("Quer sair? [s]im: ").lower().startswith('s')

    if sair is True:
        break
    else:
        continue