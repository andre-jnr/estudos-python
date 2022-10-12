n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite outro valor: "))
n4 = int(input("Digite outro valor: "))
print()

numeros = (n1, n2, n3, n4)
contador9 = contador_pares = 0

for numero in numeros:
    if numero == 9:
        contador9 += 1
    if numero % 2 == 0:
        contador_pares += 1

if contador9 == 0:
    print("O 9 não foi digitado nenhuma vez!")
else:
    print(f"O 9 foi digitado {contador9} vezes")

try:
    print(f"O 3 foi digitado pela 1° vez na posição: {numeros.index(3)+1}")
except:
    print(f"O 3 não foi digitado nenhuma vez")

if contador_pares == 0:
    print("Nenhum número par foi digitado!")
else:
    print(f"Foram digitados {contador_pares} números pares")
