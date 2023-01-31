jogadores = []
jogador = {}
gols = []

while True:
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input('Quantas partidas jogadas: '))
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {i}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    gols.clear()
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar[n/s]: '))
        if resp in 'SsNn':
            break
    if resp in 'Nn':
        break

print('-=' * 30)
# Só quis adiconar esse laço que o prof usou, achei mais interessante do que minha tática.
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>4}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-' * 40)

print()

while True:
    escolhido = int(input('Mostrar dados de qual jogador: '))
    if escolhido == 999:
        print('-' * 60)
        break
    # poderia ter usado o len(jogadores aqui)
    elif escolhido > jogadores.index(jogadores[-1]):
        print('ERRO! Não existe jogador com esse código! Tente novamente.')
        print('-' * 60)
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[escolhido]["nome"]}')
        for partida, gol in enumerate(jogadores[escolhido]["gols"]):
            print(f'    na partida {partida}, fez {gol} gols.')
        print('-' * 60)

print('<< VOLTE SEMPRE >>')
