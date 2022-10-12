from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(
    1, 100), randint(1, 100), randint(1, 100))

print(f"Os valores sorteados foram: ", end='')
for numero in numeros:
    print(numero, end=' ')
print(f" \nO menor valor gerado: {min(numeros)}")
print(f"O maior valor gerado: {max(numeros)}")
