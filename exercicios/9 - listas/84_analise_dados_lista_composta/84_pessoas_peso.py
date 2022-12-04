pessoas = []
dados = []
pesos = []
pessoas_pesadas = []
pessoas_leves = []


while True:
    dados.append(str(input("Nome: ")))
    peso = float(input("Peso: "))
    dados.append(peso)
    pesos.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    opcao = input("Deseja continuar[s/n]: ")
    if opcao in "Nn":
        break

media = sum(pesos) / len(pesos)

for pessoa in pessoas:
    if pessoa[1] > media:
        pessoas_pesadas.append(pessoa)
    else:
        pessoas_leves.append(pessoa)

print("-=" * 10)
print(f"Pessoas mais pesadas")
for pessoa in pessoas_pesadas:
    print(f"{pessoa[0]:.<10}", end='')
    print(f"{pessoa[1]:.>10}")

print("-=" * 10)
print(f"Pessoas mais leves")
for pessoa in pessoas_leves:
    print(f"{pessoa[0]:.<10}", end='')
    print(f"{pessoa[1]:.>10}")

print("-=" * 12)
print("Pessoas cadastradas: ", len(pessoas))
print("-=" * 12)
