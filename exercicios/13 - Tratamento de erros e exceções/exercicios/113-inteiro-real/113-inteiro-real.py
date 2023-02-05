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


def leia_real(msg):
    while True:
        try:
            real = float(input(msg))

        except (ValueError, TypeError):
            print('Você digitou um número inválido!')
            continue

        except KeyboardInterrupt:
            print('O usuário prefiriu não informar o solicitado')
            real = 0
            return real

        else:
            return real


inteiro = leia_inteiro('Digite um número inteiro: ')
real = leia_real('Digite um número real: ')

print()

print(f'Inteiro: {inteiro}')
print(f'Real: {real}')
