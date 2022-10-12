s = int(input('Valor do saque: '))
tc = t20 = t10 = t1 = 0
while True:
    if s >= 50:
        s -= 50
        tc += 1
    if tc >= 1:
        print(f'Foram tiradas {tc} cédulas de 50')
    elif s >= 20:
        s -= 20
        t20 += 1
    if t20 >= 1:
        print(f'Foram tiradas {t20} cédulas de 20')
    elif s >= 10:
        s -= 10
        t10 -= 1
    if t10 >= 1:
        print(f'Foram tiradas {t10} cédulas de 10')
    elif s < 10:
        s -= 1
        t1 + 1
    if t1 >= 1:
        print(f'Foram tiradas {t1} cédulas de 1')
    else:
        break
