print('-' * 20)
print('sequência Fibonacci')
print('-' * 20)
s = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print(t1, t2, end=' ')
c = 3
while c <= s:
    t3 = t1 + t2
    c += 1
    print(t3, end=' ')
    t1 = t2
    t2 = t3
print('')
print('-' * 20)
