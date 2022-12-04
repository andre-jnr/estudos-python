matriz = []
linhas = int(input("Quantas linhas você quer: "))
colunas = int(input("Quantas colunas você quer: "))

for i in range(linhas):
    matriz.append([])

for linha in range(linhas):
    for coluna in range(colunas):
        matriz[linha].append(
            input(f"Digite um valor para [{linha}, {coluna}]: "))

print()

for linha in matriz:
    for elemento in linha:
        print(f"[{elemento:^5}]", end='')
    print()
