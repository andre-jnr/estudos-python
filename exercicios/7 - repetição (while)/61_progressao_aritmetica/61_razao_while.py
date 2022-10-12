print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = pt
c = 1

while c <=10:
  print(t, end=' ')
  t += r
  c += 1
