from time import sleep


def contador(inicio, fim, passo):
    c = inicio
    if passo < 0:
        passo = abs(passo)
    if passo == 0:
        passo = 1
    if inicio < fim:
        while c < fim + 1:
            print(c, end=' ', flush=True)  # Vi na versao_prof
            sleep(0.5)
            c += passo
        print('FIM!')
    else:
        while c > fim - passo:
            print(c, end=' ', flush=True)
            sleep(0.5)
            c -= passo
        print('FIM!')


print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('-=' * 20)

print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
print('-=' * 20)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
