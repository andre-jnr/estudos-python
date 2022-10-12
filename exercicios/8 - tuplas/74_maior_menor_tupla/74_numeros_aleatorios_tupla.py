from random import randint

n1 = n2 = n3 = n4 = n5 = 0

for i in range(1, 6):
    if i == 1:
        n1 = randint(0, 100)
    if i == 2:
        n2 = randint(0, 100)
    if i == 3:
        n3 = randint(0, 100)
    if i == 4:
        n4 = randint(0, 100)
    if i == 5:
        n5 = randint(0, 100)

numeros = (n1, n2, n3, n4, n5)

print(numeros)
print(f"O menor valor gerado: {min(numeros)}")
print(f"O maior valor gerado: {max(numeros)}")
