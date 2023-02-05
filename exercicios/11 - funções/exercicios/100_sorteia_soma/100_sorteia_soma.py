from random import randint


def sorteiaLista():
    lista = []
    for i in range(5):
        lista.append(randint(0, 10))
    return lista


def somandoPares(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    return soma


lista = sorteiaLista()
print(f'Sorteando 5 valores da lista: ', end=' ')

for valor in lista:
    print(valor, end=' ')
print('PRONTO!')

print(f'Somando os números pares de {lista}, temos {somandoPares(lista)}')
