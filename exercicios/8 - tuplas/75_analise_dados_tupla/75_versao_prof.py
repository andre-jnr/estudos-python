numeros = (int(input("Digite um número: ")),
           int(input("Digite outro número: ")),
           int(input("Digite outro número: ")),
           int(input("Digite outro número: ")))

print(f'Você digitou os valores: {numeros}')

if 9 in numeros:
    print(f'O número 9 foi digitado {numeros.count(9)} vezes')
else:
    print('O número 9 foi digitado nunhuma vez')

if 3 in numeros:
    print(
        f'O número 3 foi digitado pela primeria vez na {numeros.index(3)+1}ª posição')
else:
    print('O número 3 foi digitado nenhuma vez')

print('Os valores pares digitados foram: ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' | ')
