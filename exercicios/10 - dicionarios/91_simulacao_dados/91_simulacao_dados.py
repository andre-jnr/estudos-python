from random import randint
from time import sleep

jogadas = dict()
ranking = dict()

for i in range(1, 5):
    jogadas[f'jogador{i}'] = randint(1, 6)

for key, value in jogadas.items():
    print(f'O {key} tirou {value}')
    sleep(1)

ranking = sorted(jogadas.items(), key=lambda item: item[1], reverse=True)

print(f'{"Ranking":-^25}')
for posicao, jogador in enumerate(ranking):
    print(
        f'{posicao + 1}° lugar: {ranking[posicao][0]} com {ranking[posicao][1]}')
    sleep(1)
