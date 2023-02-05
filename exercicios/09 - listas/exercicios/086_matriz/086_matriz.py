matriz = [[], [], []]

for i in range(3):
    for c in range(3):
        matriz[i].append(input(f"Digite um valor para [{i}, {c}]: "))

print()

for lista in matriz:
    for elemento in lista:
        print(f"[{elemento:^5}]", end=' ')
    print()
