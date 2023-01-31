from random import randint
v = 0
print('=-' * 20)
while True:
    pc = randint(1, 10)
    e = input('Você quer ser Par ou Impar? [P/I]').lower().strip()[0]
    while e not in 'PpIi':
        e = input('Você quer ser Par ou Impar? [P/I]').lower().strip()[0]
    n = int(input('Escolha um número: '))
    r = pc + n
    if e == 'p' and r % 2 == 0 or e == 'i' and r % 2 != 0:
        print(f'O computador escolheu {pc}, e você {n}')
        print('Logo você GANHOU!!!')
        v += 1
        print('-=' * 20)
    else:
        print(f'O computador escolheu {pc}, e você {n}')
        print('Logo você PERDEU!!!')
        print(f'Mas parabéns, você ganhou {v} vezes')
        break
