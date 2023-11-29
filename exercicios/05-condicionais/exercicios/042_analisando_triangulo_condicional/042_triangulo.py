r1 = float(input("Digite primeiro segmento:"))
r2 = float(input("Digite primeiro segmento:"))
r3 = float(input("Digite primeiro segmento:"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM formar um triangulo!")
    if r1 == r2 and r2 == r3:
        print('O triangulo é equilátero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('O triangulo é Isósceles')
    else:
        print('O triangulo é escaleno')
else:
    print("Os segmentos acima NÃO PODEM formar um triangulo!")
