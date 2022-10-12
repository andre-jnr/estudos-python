from math import factorial
var = 'Fatorial'
print(var.center(20, '-'))
n = int(input('Digite um número: '))
f = factorial(n)
print(f'{n}! = ', end='')
c = n
while c > 0:
  print(c, end=' ')
  print('x' if c > 1 else '=', end=' ')
  c -= 1
print(f' {f}')