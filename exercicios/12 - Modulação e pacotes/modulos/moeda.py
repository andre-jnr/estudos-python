def moeda(valor):
    return f'R${valor}'


def metade(valor, formatacao=False):
    metade = valor / 2
    if formatacao:
        return moeda(metade)
    else:
        return metade


def dobro(valor, formatacao=False):
    dobro = valor * 2
    if formatacao:
        return moeda(dobro)
    else:
        return dobro


def aumentar(valor, porcentagem, formatacao=False):
    valor_aumentar = (valor / 100) * porcentagem
    resultado = valor + valor_aumentar
    if formatacao:
        return moeda(resultado)
    else:
        return resultado


def diminuir(valor, porcentagem, formatacao=False):
    valor_diminuir = (valor / 100) * porcentagem
    resultado = valor - valor_diminuir
    if formatacao:
        return moeda(resultado)
    else:
        return resultado


def resumo(valor, porcentagem_aumento, porcentagem_reducao):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)

    print(f'{"Preço analisado: ":<15}', end='')
    print(f'{moeda(valor):>14}')

    print(f'{"Dobro do preço: ":<15}', end='')
    print(f'{dobro(valor, True):>15}')

    print(f'{porcentagem_aumento}% de aumento: ', end='')
    print(f'{aumentar(valor, porcentagem_aumento, True):>15}')

    print(f'{porcentagem_reducao}% de redução: ', end='')
    print(f'{diminuir(valor, porcentagem_reducao, True):>15}')

    print('-' * 30)
