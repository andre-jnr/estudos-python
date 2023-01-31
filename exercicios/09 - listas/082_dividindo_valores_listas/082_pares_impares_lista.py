valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar: ')).lower()
    if opcao in 'naonão':
        break

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'\nForam digitado os valores: {valores}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números impares digitados foram {impares}')
