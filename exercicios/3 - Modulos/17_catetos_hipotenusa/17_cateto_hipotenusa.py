from math import hypot

cateto = float(input('Qual o comprimeto do cateto:'))
ca2 = float(input('Qual o comprimento do cateto adjacente:'))
hipotenusa = hypot(cateto, ca2)
print(f'A hipotenusa vai medir:{hipotenusa}')