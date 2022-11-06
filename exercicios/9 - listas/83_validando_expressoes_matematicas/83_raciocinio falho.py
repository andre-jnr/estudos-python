# Código errado, pois não detectei todas as possibilidades de expressões erradas,
# tipo: a + b ) - c + d (
# essa expressão estaria errada, mas meu sistema dectaria que estava correto. Mas gostaria de deixar registrado meu racocinio para estudar depois.
abertos = []
fechados = []

usuario = input('Digite uma expressão: ')
for parenteses in usuario:
    if parenteses == '(':
        abertos.append(parenteses)
    if parenteses == ')':
        fechados.append(parenteses)

if len(abertos) == len(fechados):
    print('Sua expressão é valida!')
else:
    print('Sua expressão é INVÁLIDA!!!')
