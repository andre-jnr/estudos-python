resposta = 'S'
valores = list()

while resposta in 'Ss':
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
    valores.sort()
    resposta = input('Você quer continuar[S/N]: ').upper()
    print(valores)
