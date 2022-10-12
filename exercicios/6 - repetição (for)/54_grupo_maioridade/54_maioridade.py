from datetime import date

atual = date.today().year
menor = 0
maior = 0

for ordem in range(0, 7):
  nasc = int(input(f'Em que ano a {ordem + 1}º pessoa nasceu:'))
  if atual - nasc >= 18:
    maior += 1
  else:
    menor += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E {menor} pessoas menores de idade.')