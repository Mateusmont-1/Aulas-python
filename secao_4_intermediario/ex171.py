def soma_lista(l1:list, l2:list):
    return [ x + y for x, y in zip(l1, l2)]

lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_concatenada = soma_lista(lista_a, lista_b)
print(lista_concatenada)


# Uma outra possibilidade é usar zip_longest para capturar os valores da lista maior.
# from itertools import zip_longest
 
# lista_a = [10, 2, 3, 4, 5]
# lista_b = [12, 2, 3, 6, 50, 60, 70]
# lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
# print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]