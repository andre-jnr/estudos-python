casa = float(input('Digite o valor da casa R$'))
salario = float(input('Digite o valor de seu salario R$'))
anos = int(input('Em quantos anos você quer pagar:'))
prestação = casa / (anos * 12)

if prestação >= salario * 0.30:
    print("Emprestimo negado!")
else:
    print(f"""Parabens, emprestimo aprovado!
O seu emprestimo ficou no valor de {prestação:.2f}""")