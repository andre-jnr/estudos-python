s = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
while s not in 'MF':
  s = str(input('Comando inválido, por favor, digite seu sexo [M/F]:')).strip().upper()[0]
