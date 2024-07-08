
# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())


# dessa forma valor final acumula todas concatenação
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)

# teste 
# dessa forma ele só concatena o "a" inicial com a outra letra que eu concatenar

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        # nonlocal valor_final
        texto = valor_final + valor_a_concatenar 
        return texto
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)

