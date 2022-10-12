n = c = 0
lista = []
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    c += 1
    lista.append(n)
print(
    f'Foram digitados {c - 1} números, e a soma entre ele é {sum(lista) - 999}.')
