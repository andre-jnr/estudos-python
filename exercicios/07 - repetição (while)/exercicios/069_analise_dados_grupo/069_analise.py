p18 = h = m20 = 0
while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').upper().strip()[0]
    while sexo not in 'FM':
        sexo = input('Sexo [F/M]: ').upper().strip()[0]
    continuar = input('Você quer continuar? [S/N] ').upper().strip()[0]
    if idade > 19:
        p18 += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    while continuar not in 'SN':
        continuar = input('Você quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        print('-=' * 20)
        print(f'{p18} pessoas tem mais de 20 anos')
        print(f'{h} homens foram cadastrados')
        print(f'{m20} melhures tem menos de 20 anos')
        break
