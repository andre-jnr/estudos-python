extensos = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUARTO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
            'DOZE', 'TREZE', 'CARTOZE', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
programa = 'sim'

while programa == 'sim':
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou {extensos[numero].upper()}')
    while True:
        print('Você quer continuar?')
        programa = str(input()).lower()
        if programa == 'sim' or programa == 'não':
            break
        print('Não entendi.', end=' ')
print('Bye bye!')
