valores = []
# Na versão do prof eu vi que poderia declara assim: valores = [[],[]]

valores.append(list())
valores.append(list())

for i in range(1, 8):
    valor = int(input(f"Digite o {i}° valor: "))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print("Números pares digitados: ", valores[0])
print("Números impares digitados: ", valores[1])
