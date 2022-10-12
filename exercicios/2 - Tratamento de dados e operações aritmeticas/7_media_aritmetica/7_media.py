# calcular média de um aluno
aluno = input('Qual aluno vamos calcular a média? ')
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
m = (n1+n2+n3)/3
print(f'A média de {aluno} é {m:.2f}')