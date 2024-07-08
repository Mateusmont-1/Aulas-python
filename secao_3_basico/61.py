import re
import sys
entrada = input('CPF: ')
cpf_str = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_str[:9]
letra = 0
soma_digito_1 = 0
soma_digito_2 = 0
try:
    cpf_int = int(cpf_str)
except ValueError:
    print('Digite o CPF corretamente')

for x in range(10, 1, -1):
    digito = int(cpf_str[letra])
    soma_digito_1 += digito * x
    letra += 1

letra = 0

for x in range(11, 1, -1):
    digito = int(cpf_str[letra])
    soma_digito_2 += digito * x
    letra += 1

verificacao_prim_dig = (soma_digito_1 *10) % 11
verificacao_prim_dig = verificacao_prim_dig if verificacao_prim_dig <= 9 else 0

verificacao_segund_dig = (soma_digito_2 *10) % 11
verificacao_segund_dig = verificacao_segund_dig if verificacao_segund_dig <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{verificacao_prim_dig}{verificacao_segund_dig}'

if cpf_str == cpf_gerado_pelo_calculo:
    print(f'{cpf_str} é válido')

else:
    print(f'{cpf_str} é invalido')