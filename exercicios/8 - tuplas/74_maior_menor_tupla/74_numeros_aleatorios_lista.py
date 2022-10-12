import random

numeros = []

for i in range(6):
    numero = random.randint(0, 100)
    numeros.append(numero)

print(numeros)
print(f"O menor valor gerado: {min(numeros)}")
print(f"O maior valor gerado: {max(numeros)}")
