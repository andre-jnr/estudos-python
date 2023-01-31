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
    resp = str(input('Deseja continuar[n/s]: '))
    if resp in 'Nn':
        break
print('-=' * 30)

print(f'{"cod":>3}', end=' ')
print(f"{'nome':<10}", end=' ')
print(f'{"gols":<13}', end=' ')
print(f'{"total":<5}')
print('-' * 35)

for j in jogadores:
    print(f'{jogadores.index(j):>3}', end=' ')
    print(f'{j["nome"]:<10}', end=' ')
    print(f'{str(j["gols"]):<13}', end=' ')
    print(f'{j["total"]}')
print()

while True:
    escolhido = int(input('Mostrar dados de qual jogador: '))
    if escolhido == 999:
        print('-' * 60)
        break
    elif escolhido > jogadores.index(jogadores[-1]):
        print('ERRO! Não existe jogador com esse código! Tente novamente.')
        print('-' * 60)
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[escolhido]["nome"]}')
        for partida, gol in enumerate(jogadores[escolhido]["gols"]):
            print(f'    na partida {partida}, fez {gol} gols.')
        print('-' * 60)

print('<< VOLTE SEMPRE >>')
