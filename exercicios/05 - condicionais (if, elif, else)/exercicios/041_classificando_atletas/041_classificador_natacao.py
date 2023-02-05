from datetime import date
ano = int(input('Digite o ano de nascimento:'))
idade = date.today().year - ano

print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Sua categoria é mirim')
elif idade <= 14:
    print('Sua categoria é infantil')
elif idade <= 19:
    print('Sua categoria é junior')
elif idade == 20:
    print('Sua categoria é sênior')
elif idade > 20:
    print('Sua categoria é master')