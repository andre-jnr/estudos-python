from math import hypot

cateto = float(input('Qual o comprimeto do cateto:'))
cateto_adjacente = float(input('Qual o comprimento do cateto adjacente:'))
hipotenusa = hypot(cateto, cateto_adjacente)
print(f'A hipotenusa vai medir:{hipotenusa}')
