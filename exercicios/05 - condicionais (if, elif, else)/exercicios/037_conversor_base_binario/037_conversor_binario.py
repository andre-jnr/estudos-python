numero = int(input('Digite um número inteiro: '))

print('''
Escolha uma das bases para conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal
''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'Convertido para binário: {bin(numero)[2:]}')

elif opcao == 2:
    print(f'COnvertido para octal: {oct(numero)[2:]}')

elif opcao == 3:
    print(f'Convertido para hexadecimal: {hex(numero)[2:]}')

else:
    print('Opção inválida!')
