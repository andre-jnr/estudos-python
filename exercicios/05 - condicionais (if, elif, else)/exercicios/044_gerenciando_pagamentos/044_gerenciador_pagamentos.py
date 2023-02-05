preço = float(input('Qual o preço da compra:'))
parcela = int(input('Você vai pagar de quantas vezes:'))
print('[1] - cheque')
print('[2] - cartão')
forma = int(input('Qual a forma de pagamento:'))

if parcela == 1 and forma == 1:
    print(f'Em {parcela}x, ficou de R${preço - (preço * 0.10):.2f}')
elif parcela == 1 and forma == 2:
    print(f'Em {parcela}x, ficou de R${preço - (preço * 0.05):.2f}')
elif parcela == 2 and forma == 2:
    print(f'Em {parcela}x, cada parcela fica de  R${preço / 2:.2f}')
else:
    print(f'Em {parcela}, cada parcela fica à R${(preço + preço * 0.20) / parcela}')