def ficha(nome='', gols=0):
    if nome == '':
        print(f'O jogador {"<desconhecido>"}', end='')
    else:
        print(f'O jogador {nome}', end='')
    if gols == '':
        print(f' fez 0 gol(s) no campeonato.')
    else:
        print(f' fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = (input('Número de gols: '))

ficha(nome, gols)
