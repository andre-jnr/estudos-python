from tkinter import N


n = int(input('Digite um número:'))
t = 0

for c in range(1, n + 1):
  if n % c == 0:
    t += 1

print(f'O número é divisivel {t} vezes')

if t > 2:
  print(f'Por tanto, o número {n} NÃO é PRIMO.')
else:
  print(f'Por tanto, o número {n} É PRIMO.')
