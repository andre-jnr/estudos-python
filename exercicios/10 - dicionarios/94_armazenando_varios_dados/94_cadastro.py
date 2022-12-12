pessoa = {}
pessoas = []
idades = []
mulheres = []
p_acima_media = []

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: '))
        if pessoa['sexo'] in 'FfMm':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou  F!')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    while True:
        resposta = input('Deseja continuar[s/n]: ')
        print('-=' * 30)
        if resposta not in 'SsNn':
            print('Não entendi, por favor, digite apenas S ou N.')
        else:
            break
    if resposta in 'Nn':
        break

for p in pessoas:
    for chave, valor in p.items():
        if chave == 'idade':
            idades.append(valor)
        if chave == 'sexo' and valor in 'Ff':
            mulheres.append(p)

for p in pessoas:
    for chave, valor in p.items():
        if chave == 'idade' and valor > sum(idades) / len(idades):
            p_acima_media.append(p)

print('-=' * 30)
print(f' - O grupo tem {len(pessoas)} pessoas')
print(f' - idade média é {sum(idades) / len(idades):.0f}')

print(f' - As mulheres cadastradas foram: ', end='')
for mulher in mulheres:
    for chave, valor in mulher.items():
        if chave == 'nome':
            print(valor, end='; ')

print(f'\n - Pessoas com idade acima da média:')
for p in p_acima_media:
    for chave, valor in p.items():
        print(f'    {chave} = {valor}', end='; ')
    print('')

print('<< SISTEMA ENCERRADO! >>')
