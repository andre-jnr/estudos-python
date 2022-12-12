jogador = {}
gols = []

jogador['nome'] = str(input('Nome: '))
jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou: '))

for jogo in range(jogos):
    gols.append(
        int(input(f'Quantos gol {jogador["nome"]} fez na partida {jogo}: ')))

jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-=' * 30)
print(jogador)

print('-=' * 30)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')

print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')

for partida, gol in enumerate(gols):
    print(f'   => Na partida {partida}, fez {gol} gols.')

print(f'Foi um total de {sum(gols)}')
