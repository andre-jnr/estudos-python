print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

PT = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(PT, PT + (11 - 1) * r, r):
  print(c, end=' ')