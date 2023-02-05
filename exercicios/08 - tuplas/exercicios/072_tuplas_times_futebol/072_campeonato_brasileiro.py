campeonato = ('', 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
              'Athletico-PR', 'Atlético-MG', 'América-MG', 'Fortaleza', 'Botafogo',
              'Santos', 'Goiás', 'São paulo', 'Red bull bragantino', 'Coritiba',
              'Ceará', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')

print('-=-=Campeonato Brasileiro 10/2022-=-=')
for time in campeonato[1:]:
    print(f'{campeonato.index(time)}-{time}')
print()

print('=--==--=Os 4 últimos colocados=--==--=')
for ultimo in campeonato[-5:]:
    print(f'{campeonato.index(ultimo)}-{ultimo}')
print()

print('=-=-=-Os times em ordem alfabética-=-=-=')
for ordem in sorted(campeonato[1:]):
    print(ordem)
print()

while True:
    usuario_time = str(input('Digite um time: ')).capitalize().strip()
    if usuario_time in campeonato:
        print(f'{usuario_time} está em {campeonato.index(usuario_time)}°')
        break
    print('Desculpe, seu time não está na séria A.', end=' ')
