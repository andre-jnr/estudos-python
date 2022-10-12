from random import randint
pc = randint(1,3)

print('''[1] - Pedra
[2] - Papel
[3] - Tesoura''')
player = int(input('Escolha:'))

if pc == 1 and player == 2:
    print('A máquina escolheu PEDRA')
    print('Você ganhou!')
elif pc == 1 and player == 3:
    print('A máquina escolheu PEDRA')
    print('Você perdeu!')
elif pc == 2 and player == 1:
    print('A máquina escolheu PAPEL')
    print('Você perdeu!')
elif pc == 2 and player == 3:
    print('A máquina escolheu PAPEL')
    print('Você ganhou!')
elif pc == 3 and player == 1:
    print('A máquina escolheu TESOURA')
    print('Você ganhou!')
elif pc == 3 and player == 2:
    print('A máquina escolheu TESOURA')
    print('Você perdeu!')
elif pc == player:
    print('Empate!')
else:
    print('Comando invalido')