# soma todos os múltiplos de 3

soma = 0
quant_valores_impares = 0

for c in range(1, 501):
    if c % 3 == 0:
        quant_valores_impares += 1
        soma += c

print(
    f'A soma entre todos os {quant_valores_impares} valores, é igual a {soma}')
