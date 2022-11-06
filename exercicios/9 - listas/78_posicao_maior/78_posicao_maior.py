valores = []
for i in range(0, 5):
    i = int(input("Digite um valor: "))
    valores.append(i)

print("Os valores digitados foram: ", end=' ')
for valor in valores:
    if valores.index(valor) == valores.index(valores[-1]):
        print(f'{valor}.')
    else:
        print(valor, end=', ')

print(
    f'O maior valor foi {max(valores)}, na posição {valores.index(max(valores)) + 1}')
print(
    f'O menor valor digitado foi {min(valores)}, na posição {valores.index(min(valores)) + 1}')

# o algoritmo poderia ser desenvolvido usando duas variaveis no laço de repetição e um enumerate(lista), mas assim assim mais prático.
