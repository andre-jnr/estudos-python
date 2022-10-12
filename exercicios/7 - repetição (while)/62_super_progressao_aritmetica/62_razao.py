print('-=' * 11)
print('Progressão aritmética')
print('-=' * 11)

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
t = pt
ot = 1

while ot != 0:
    while c <= 10:
        print(t, end=' ')
        t += r
        c += 1
    print('')
    ot = int(input('Você quer mais quantos termos: '))
    print('')
    for t in range(t + r, t + (ot) * r, r):
        c += 1
        print(t, end=' ')
print(f'Progressão terminada com {c} termos.')
