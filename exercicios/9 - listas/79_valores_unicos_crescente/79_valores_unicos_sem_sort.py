resposta = 'S'
valores = list()
contador = 0

while resposta in 'Ss':
    usuario = int(input('Digite um valor: '))
    if contador == 0:
        valores.append(usuario)
        contador += 1
    else:
        if usuario not in valores:
            for posicao, valor in enumerate(valores):
                if valor > usuario:
                    valores.insert(posicao, usuario)
                    break
                else:
                    valores.append(usuario)
                    break
    resposta = input('Você quer continuar[S/N]: ').upper()
    print(valores)
