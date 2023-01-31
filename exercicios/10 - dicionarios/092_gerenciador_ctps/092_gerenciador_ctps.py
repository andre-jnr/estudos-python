from datetime import date

cadastro = {
    'nome': str(input('Nome: ')),
    'idade': int(input('Ano de nascimento: ')),
    'ctps': int(input('N° da carteira de trabalho [0 se não tiver]: ')),
}

cadastro['idade'] = date.today().year - cadastro['idade']

if cadastro['ctps'] != 0:
    cadastro['ano_contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salario: '))
    cadastro['aposentadoria'] = (cadastro['ano_contratacao'] + 35) - \
        (date.today().year - cadastro['idade'])

print('-=' * 30)

for chave, informacao in cadastro.items():
    print(f'{chave} tem o valor {informacao}.')
