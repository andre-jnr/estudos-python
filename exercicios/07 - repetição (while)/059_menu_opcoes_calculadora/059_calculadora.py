from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
o = 0
while o != 5:
  print('')
  print('[1] - somar')
  print('[2] - multiplicar')
  print('[3] - maior')
  print('[4] - novos números')
  print('[5] - sair do programa')
  o = int(input('Qual sua opção: '))
  if o == 1:
    print(f'{n1} + {n2} = {n1 + n2}')
    sleep(1)
  elif o == 2:
    print(f'{n1} X {n2} = {n1 * n2}')
    sleep(1)
  elif o == 3:
    lista = [n1, n2]
    print(f'Entre {n1} e {n2}, o maior valor é {max(lista)}.')
    sleep(1)
  elif o == 4:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    sleep(1)
  elif o == 5:
    print('Tchau!')
  else:
    print('Comando inválido')
    print('')
    sleep(1)
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
