from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMETE!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para se alistar')
else:
    print(f'Você já deveria ter se alistado há {idade - 18} anos')