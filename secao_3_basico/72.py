def multiplicacao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

def par_ou_impar(x):
    if x%2 == 0:
        return f'o numero {x} é par'
    return f'o numero {x} não é par'

print(multiplicacao(1,2,3,4,5))
print(par_ou_impar(3))
