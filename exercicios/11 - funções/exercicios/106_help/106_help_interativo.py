def help_interativo(funcao):
    help(funcao)


while True:
    opcao_usuario = input('Função ou biblioteca > ')
    help_interativo(opcao_usuario)
    if opcao_usuario == 'fim':
        break
