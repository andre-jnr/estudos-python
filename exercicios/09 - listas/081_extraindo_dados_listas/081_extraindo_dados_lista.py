lista = []
lista_reversa = []
contador = 0

while True:
    valor_usuario = int(input('Digite um número: '))
    lista.append(valor_usuario)
    lista_reversa.append(valor_usuario)
    contador += 1
    opcao = input('Deseja continuar[n/s]: ').lower()
    lista_reversa.sort(reverse=True)
    if opcao in 'naonão':
        break

print()

print(f'Foram digitados os números: ', end='')
for numero in lista:
    if lista.index(numero) == lista.index(lista[-1]):
        print(numero, end='. ')
    else:
        print(numero, end=', ')

print(f'\nForam digitados {contador} números.')

print(f'Os valores em ordem decrescente: ', end='')
for numero in lista_reversa:
    if lista_reversa.index(numero) == lista_reversa.index(lista_reversa[-1]):
        print(numero, end='. ')
    else:
        print(numero, end=', ')

if lista.count(5) <= 0:
    print(f'\nO 5 NÃO foi encontrado dentro dessa lista.')
else:
    print(f'\nO 5 FAZ parte dessa lista.')
