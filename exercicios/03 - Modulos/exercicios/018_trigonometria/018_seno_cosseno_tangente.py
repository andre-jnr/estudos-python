from math import sin, cos, tan, radians

angulo = float(input('Digite uma angulo qualquer: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'Seno: {seno:.2f}')
print(f'Consseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')
