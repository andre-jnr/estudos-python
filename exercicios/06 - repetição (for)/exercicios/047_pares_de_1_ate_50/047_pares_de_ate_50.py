print('Números pares de 1 até 50: ', end='')

for i in range(2, 51, 2):
    if i != 50:
        print(i, end=', ')

    else:
        print(i, end='.')
