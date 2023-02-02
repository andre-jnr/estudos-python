from modulo.interface import *
from modulo.arquivo import *
from time import sleep

arquivo = 'bancodedados.txt'

if arquivo_existe(arquivo):
    print('Arquivo encontrado com sucesso!')

else:
    print('arquivo NÃO encontrado')

while True:
    escolha = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas',
                    'Sair do sistema'])
    if escolha == 1:
        ler_arquivo(arquivo)
    elif escolha == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).capitalize().strip()
        idade = leia_inteiro('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif escolha == 3:
        cabecalho('Saindo do sistema... até logo!')
        break
    else:
        cabecalho('Erro! Digite uma opção válida')
        sleep(2)
