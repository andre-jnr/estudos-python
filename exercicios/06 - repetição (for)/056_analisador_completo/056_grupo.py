mi = []
mh = 0
nhv = ''
cm = 0

for p in range(1, 5):
  print(f'-' * 4, {p},'ª pessoa','-' * 4)
  nome = input('nome:').capitalize().strip()
  idade = int(input('idade:'))
  sexo = input('sexo[F/M]:').lower()
  mi.append(idade)
  if idade > mh and sexo == 'm':
    mh = idade
    nhv = nome
  elif idade <= 20 and sexo in 'f':
    cm += 1

print(f'A idade do grupo é {sum(mi) /len(mi):.0f}anos')
print(f'O homem mais velho é {nhv}, com {mh} anos')
print(f'E {cm} mulheres tem menos de 20 anos')