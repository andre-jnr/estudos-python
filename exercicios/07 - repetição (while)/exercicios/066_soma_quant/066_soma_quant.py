soma = contador = 0

while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    contador += 1
    soma += numero

print(f'A soma dos {contador} valores digitados foi {soma}!')
