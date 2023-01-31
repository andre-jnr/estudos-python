ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"N°":<3}{"Nome":<10}{"Media":>8}')
print('-' * 26)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<3}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 35)
    opcao = int(input('Mostrar notas de qual aluno? [999 para interromper] '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')

print('<<< VOLTE SEMPRE >>>')
