listagem = ('lapis', 1.74,
            'Borracha', 2,
            'Caderno', 15.90,
            'Livro', 34.90)
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)
for produto in range(0, len(listagem)):
    if produto % 2 == 0:
        print(f'{listagem[produto]:.<20}', end='')
    else:
        print(f'R${listagem[produto]:>7.2f}')
