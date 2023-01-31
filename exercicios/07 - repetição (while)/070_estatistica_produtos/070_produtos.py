t = p1000 = 0
mv = 99999
while True:
    p = input('Produto: ')
    v = float(input('Preço: '))
    t += v
    if v < mv:
        mv = v
        mp = p
    if v > 1000:
        p1000 += 1
    e = 'f'
    while e not in 'SN':
        e = input('Você quer continuar [S/N]: ').upper().strip()[0]
    if e == 'N':
        print('-=' * 20)
        print(f'Total: {t:.2f}')
        print(f'Produto mais barato: {mp}')
        print(f'Produtos acima de 1000: {p1000}')
        break
