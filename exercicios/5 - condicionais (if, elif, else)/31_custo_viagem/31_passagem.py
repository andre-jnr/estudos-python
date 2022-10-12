distancia = float(input('Qual a distância da viagem:'))
if distancia <= 200:
    va = distancia * 0.50
    print(f"A passagem fica de R${va:.2f}")
else:
    va = distancia * 0.45
    print(f"A passagem fica de R${va:.2f}")
