pessoas = []
dados = []
maior_peso = menor_peso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = input('Deseja continuar[S/N]: ')
    if resp in 'Nn':
        break

for pessoa in pessoas:
    print(pessoa)

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'As pessoas mais pesadas foram: ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print('[', pessoa[0], ']')
print(f'O menor peso foi: ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print('[', pessoa[0], ']')
