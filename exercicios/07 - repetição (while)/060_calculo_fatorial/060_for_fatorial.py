from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print(f'{n}! =', end=' ')
for c in range(n, 0, -1):
  print(c, end=' ')
  print('x' if c > 1 else '=', end=' ')
  c -= 1
print(f'{f}')