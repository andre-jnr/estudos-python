#paga R$7,00 de multa depois dos 80km
v = float(input("Digite a velocidade de seu carro:"))
if v >= 80:
    multa = (v - 80) * 7
    print(f"Sua multa foi de R${multa:.2f}")
else:
    print("Ótimo, continue seguinda as leis de segurança!")
