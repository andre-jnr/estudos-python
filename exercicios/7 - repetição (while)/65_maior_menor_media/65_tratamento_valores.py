r = 's'
c = 0
lista = []
while r == 's':
    n = int(input('Digite um número: '))
    lista.append(n)
    r = input('Você quer continuar [N/S]: ').lower()
    c += 1
print(f'Foram digitas {c} números,')
print(f'a média é {sum(lista) / len(lista)},')
print(f'o maior valor foi {max(lista)},')
print(f'o menor valor foi {min(lista)}.')
