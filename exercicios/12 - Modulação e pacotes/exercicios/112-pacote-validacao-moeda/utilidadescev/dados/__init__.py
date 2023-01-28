def leia_dinheiro(msg):
    while True:
        valor = str(input(msg)).replace(',', '.')
        if (valor.isalpha()) or (valor.strip() == '') or (valor.count('.') > 1):
            print(f'ERRO! "{valor}" não é um preço válido!')
        else:
            return float(valor)
