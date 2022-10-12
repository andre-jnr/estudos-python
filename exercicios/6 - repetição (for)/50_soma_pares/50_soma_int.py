s = 0
cont = 0
ct = 0

for c in range(0, 6):
  n = int(input('Digite um número: '))
  ct += 1
  if n % 2 == 0:
    s += n
    cont += 1

print(f'De todos os {cont} números pares, a soma é {s}')
print(f'De {ct} números informados.')