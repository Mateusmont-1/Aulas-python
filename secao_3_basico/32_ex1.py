numero_str = input('Digite um número inteiro:')

if numero_str.isdigit():
    numero_int = int(numero_str)
    par_inpar = numero_int % 2 == 0
    par_inpar_str = 'ímpar'
    if par_inpar:
        par_inpar_str = 'par'
    print(f'O número {numero_int} é {par_inpar_str}')
else:
    print('Não é um número inteiro')