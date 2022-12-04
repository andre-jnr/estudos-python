alunos = []
dados = []

while True:
    dados.append(str(input("Nome: ")).capitalize())
    dados.append(float(input("Nota 1: ")))
    dados.append(float(input("Nota 2: ")))
    alunos.append(dados[:])
    dados.clear()
    print("-" * 15)
    resposta = input("Deseja continuar[s/n]: ")
    if resposta in "Nn":
        break
print(" ")

print(f'{"Cod":<3}', end="")
print(f'{"Nome":^10}', end="")
print(f'{"Media":>8}')
print("--" * 10)

for cod, aluno in enumerate(alunos):
    print(f'{cod:<3}', end='')
    print(f'{aluno[0]:^10}', end='')
    print(f"{sum(aluno[1:]) / 2:^10}")
print(" ")

print("Digite o código do aluno abaixo, ou 999 para interromper")

while True:
    notas_aluno = int(input("Mostrar nota de algum aluno: "))
    if notas_aluno > alunos.index(alunos[-1]):
        break
    print(
        f'As notas de {alunos[notas_aluno][0]} foram: {alunos[notas_aluno][1:]}')
    print('-' * 30)

print("Programa finalizado")
