print('{:=^40}'.format('Lojas Junior'))
preço = float(input('Digite o preço das compras: R$'))
print('{:-^40}'.format('FORMA DE PAGAMENTO'))
print('''[1] - à vista dinheiro/cheque
[2] - à vista no cartão
[3] - 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual a forma de pagamento:'))

if opção == 1:
    print(f'Sua compra de R${preço:.2f} vai ficar de {preço - (preço * 0.10):.2f}')
elif opção == 2:
    print(f'Sua compra de R${preço:.2f} vai ficar de {preço - (preço * 0.05):.2f}')
elif opção == 3:
    print(f'Sua compra de R${preço:.2f}, foi parcelada em 2x de {preço / 2 :.2f}')
elif opção == 4:
    parcela = (int(input('Quantas parcelas:')))
    print(f'Sua compra de R${preço:.2f}, foi parcelada em {parcela}x de {(preço + (preço *20)) / parcela :.2f}')
    print(f'Com o total de {preço + (preço * 0.20):.2f}')
else:
    print('Opção inválida de pagamento!')