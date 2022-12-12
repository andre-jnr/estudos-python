ficha = dict()

ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input('Media: '))

if ficha['media'] < 5:
    ficha['situacao'] = 'reprovado!'
else:
    ficha['situacao'] = 'aprovado!'

print('-=' * 15)

for chave, valor in ficha.items():
    try:
        print(f'{chave}: {valor:.2f}')
    except:
        print(f'{chave}: {valor}')
