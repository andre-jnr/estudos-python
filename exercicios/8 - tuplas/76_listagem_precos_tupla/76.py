listagem = ('Pão', 2.5, 'Frango', 18.5, 'Açaí', 1, 'feijão', 5)
print("-" * 30)
print('LISTAGEM DE PREÇOS')
for i in range(0, len(listagem), 2):
    print(f'{listagem[i]}............{listagem[i+1]}')
print("-" * 30)
