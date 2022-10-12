pesos = []

for ordem in range(0, 5):
  peso = float(input(f'Digite o peso da {ordem + 1}º pessoa:'))
  pesos.append(peso)

print(f'O maior peso foi {max(pesos):.2f}Kg')
print(f'O menor peso foi {min(pesos):.2f}Kg.')