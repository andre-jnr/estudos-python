n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro valor:"))

if n1 > n2:
    print(f"{n1} é maior que {n2} ")
elif n1 < n2:
    print(f"{n1} é menor que {n2}")
else:
    print("Não existe número maior, os dois não iguais!")