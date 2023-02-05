from modulo.interface import *


def arquivo_existe(arquivo):
    try:
        with open(arquivo, 'r') as file:
            file.read()
    except FileNotFoundError:
        with open(arquivo, 'w') as file:
            file.write('')
    else:
        return True


def ler_arquivo(arquivo):
    try:
        a = open(arquivo, 'r')
    except:
        print('Erro ao ler aquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'a')
    except:
        print('Houve um erro ao tentar ler o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houver um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso.')
            a.close()
