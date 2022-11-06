numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não será adicionado...')
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print('Você digitou os números: ', numeros)
