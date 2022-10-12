from random import randint
v = 0
while True:
    e = input('Você quer PAR ou ÍMPAR? [P/I] ').lower().strip()[0]
    while e not in 'PpIi':
        e = input('Você quer PAR ou ÍMPAR? [P/I] ').lower().strip()[0]
    n = int(input('Digite um número: '))
    pc = randint(1, 10)
    r = n + pc
    if e == 'p':
        if r % 2 == 0:
            print(
                f'O computador escolheu {pc}, e você {n}, o total foi {r}, Deu PAR')
            print(f'Logo, você GANHOU!!!')
            v += 1
        else:
            print(
                f'O computador escolheu {pc}, e você {n}, o total foi {r}, Deu IMPAR,')
            print('Logo, você PERDEU!!!')
            print(f'Mas não fique triste, você tem um total de {v} vitórias')
            break
    if e == 'i':
        if r % 2 != 0:
            print(
                f'O computador escolheu {pc}, e você {n}, o total foi {r}, Deu IMPAR')
            print(f'Logo, você GANHOU!!!')
            v += 1
        else:
            print(
                f'O computador escolheu {pc}, e você {n}, o total foi {r}, Deu PAR,')
            print('Logo, você PERDEU!!!')
            print(f'Mas não fique triste, você tem um total de {v} vitórias')
            break
