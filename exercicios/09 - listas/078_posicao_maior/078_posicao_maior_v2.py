# Quando o professor executou a versão dele percebi que ele queria assim:
valores = []
for valor in range(0, 5):
    valor = int(input(f'Digite um valor na posição {valor}: '))
    valores.append(valor)

if valores.count(max(valores)) > 1:
    print(
        f'O maior valor digitado foi {max(valores)}, nas posições: ', end='')
    for posicao, valor in enumerate(valores):
        if valor == max(valores):
            print(posicao, end='... ')
else:
    print(
        f'O maior valor digitado foi {max(valores)}, na posição: {valores.index(max(valores))}', end='')

if valores.count(min(valores)) > 1:
    print(
        f'\nO menor valor digitado foi {min(valores)}, nas posições: ', end='')
    for posicao, valor in enumerate(valores):
        if valor == min(valores):
            print(posicao, end='... ')
else:
    print(
        f'\nO menor valor digitado foi {min(valores)}, na posição: {valores.index(min(valores))}')
