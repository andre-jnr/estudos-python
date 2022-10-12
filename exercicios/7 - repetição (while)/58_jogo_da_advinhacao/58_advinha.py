from random import randint
def jogar():
  try:
    m = randint(1, 10)
    c = 0
    
    print('Acabei de pensar num número entre 1 á 10.')
    print('Será que você consegue adivinhar qual foi?')
    n = int(input('Qual seu palpite? '))
    while m != n:
      c += 1
      if n < 11:
        if n < m:
          n = int(input('É um número maior, tente novamente: '))
        elif n > m:
          n = int(input('É um número menor, tente novamente:'))
      else:
        n = int(input('Não esqueça, é um número entre 1 à 10, tente novamente:'))
    print(f'Caraca, você errou {c} vezes')
    escolha()
  except:
    print('Comando inválido!')
    jogar()

def certeza():
  try:
    print('[1] - SIM')
    print('[2] - NÃO')
    c = int(input('Você tem certeza? '))
    if c == 2:
      escolha()
    else:
      print('Tchau!')
  except:
    print('Desculpa, não entendi')
    escolha()

def escolha():
  try:
    print('[1] - SIM')
    print('[2] - NÃO')
    e = int(input('Você deseja joga novamente? '))
    if e == 1:
      jogar()
    else:
      certeza()
  except:
    print('Desculpa, não entendi')
    escolha()
    
jogar()