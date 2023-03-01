n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

media = (n1 + n2) / 2
print(f'Média: {media}')

if media >= 7:
    print('APROVADO!')

elif media <= 6.9:
    print('RECUPERAÇÂO')

elif media < 5:
    print('REPROVADO')
