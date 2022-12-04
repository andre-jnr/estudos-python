from random import randint
from time import sleep

lista = list()
jogos = list()

print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total_jogos = 1

while total_jogos <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    total_jogos += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

print('-=' * 3, f' SORTEANDO {quantidade} JOGOS', '-=' * 3)

for indice, lista in enumerate(jogos):
    print(f'{indice + 1}° jogo sorteado: {lista}')
    sleep(1)

print('-=' * 5, '< BOA SORTE>', '-=' * 5)
