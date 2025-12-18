# soma todos os múltiplos de 3

soma = 0

for c in range(0, 501, 3):
    soma += c

print(
    f'A soma de todos os multiplos de 3, de 1 até 500, é igual a {soma}')
