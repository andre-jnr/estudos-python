while True:
    n = int(input('Digite um número: '))
    print('=' * 11)
    for c in range(1, 11):
        print(f'{c}X{n} = {c * n}')
    print('=' * 11)
    if n < 0:
        print('Tchau')
        break
