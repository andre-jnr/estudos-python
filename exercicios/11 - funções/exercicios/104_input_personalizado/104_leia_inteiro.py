def leiaInt(texto):
    while True:
        try:
            numero = input(texto)
            return int(numero)
        except:
            print('\033[31mValor invalido!\033[m')


n = leiaInt('Digite um número: ')
print(n)
