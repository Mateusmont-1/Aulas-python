primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)
if int_primeiro_valor > int_segundo_valor:
    print(f'primeiro_valor={primeiro_valor} é maior que o segundo_valor={segundo_valor}')

elif int_segundo_valor > int_primeiro_valor:
    print(f'segundo_valor={segundo_valor} é maior que o primeiro_valor={primeiro_valor}')

else:
    print(f'O primeiro_valor={primeiro_valor} é igual ao segundo_valor={segundo_valor}')