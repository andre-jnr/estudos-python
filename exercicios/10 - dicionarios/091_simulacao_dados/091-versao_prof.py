from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jegador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking = list()

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('=== RANKING DOS JOGADORES ===')
for indice, valor in enumerate(ranking):
    print(f'    {indice + 1}° lugar: {valor[0]} com {valor[1]}')
