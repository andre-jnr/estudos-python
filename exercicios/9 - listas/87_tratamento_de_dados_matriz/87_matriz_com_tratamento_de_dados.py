matriz = [[], [], []]
soma_pares = soma_segunda_coluna = 0

for i in range(3):
    for c in range(3):
        valor = int(input(f"Digite o valor [{i}, {c}]: "))
        matriz[i].append(valor)
        if valor % 2 == 0:
            soma_pares += valor

for lista in matriz:
    soma_segunda_coluna += lista[-1]
    for elemento in lista:
        print(f"[{elemento:^5}]", end=' ')
    print()

print("A soma de todos os pares digitados: ", soma_pares)
print("A soma da terceira coluna: ", soma_segunda_coluna)
print("O maior valor da segunda linha: ", max(matriz[1]))
