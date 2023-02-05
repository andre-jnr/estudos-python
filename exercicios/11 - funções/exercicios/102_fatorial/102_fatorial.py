def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número.
    :param numero: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de n
    """
    if show == False:
        resultado = 1
        for i in range(numero, 1, -1):
            resultado *= i
        resultado = '{:,}'.format(resultado)
        return resultado
    else:
        resultado = 1
        for i in range(numero, 1, -1):
            print(i, end='x')
            resultado *= i
        resultado = '{:,}'.format(resultado)
        print('1=', resultado)


numero = int(input('Digite um número: '))
while True:
    formato = str(input('Mostrar calculo[n/s]: ')).strip().lower()
    if formato in ['s', 'n']:
        if formato == 's':
            print(fatorial(numero, show=True))
            break
        else:
            print(fatorial(numero))
            break
