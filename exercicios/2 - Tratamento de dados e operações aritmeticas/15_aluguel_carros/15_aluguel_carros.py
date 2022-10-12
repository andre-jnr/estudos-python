km  = float(input('Quantos quilometros rodados?'))
dias = int(input('Quantos dias alugados?'))
v = (dias*60)+(km*0.15)
print(f'O total a pagar é de R${v:.2f}')