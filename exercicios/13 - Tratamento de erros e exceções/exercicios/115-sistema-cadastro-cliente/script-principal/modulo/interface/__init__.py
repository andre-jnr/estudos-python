def leia_inteiro(msg):
    while True:
        try:
            inteiro = int(input(msg))

        except (ValueError, TypeError):
            print('Você digitou um número inválido!')
            continue

        except KeyboardInterrupt:
            print('O usuário prefiriu não informar o solicitado')
            inteiro = 0
            return inteiro

        else:
            return inteiro


def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(opcoes):
    cabecalho('MENU PRINCIPAL')
    for indice, opcao in enumerate(opcoes):
        print(f'{indice + 1} - {opcao}')
    print(linha())
    escolha = leia_inteiro('Sua opção: ')
    return escolha
