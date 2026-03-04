'''
Crie a classe caneta, que simule o
funcionamento de uma caneta colorida,
podendo escrever frases na cor relativa.
'''
from rich import print

class Caneta:
  def __init__(self, cor, tampar=True):
    self.cor = cor
    self.tampar = tampar


  def destampar(self):
    self.tampar = False

  
  def tampar(self):
    self.tampar = True


  def escrever(self, frase=''):
    cores_disponiveis = {
      'azul': 'blue',
      'vermelho': 'red',
      'verde': 'green',
      'amarelo': 'yellow'
    }

    if not self.tampar:
      print(f'[{cores_disponiveis[self.cor]}]{frase}[/]', end='')
    else:
      print(f'🚫 A [{cores_disponiveis[self.cor]}]Caneta[/] está tampada!')

    
  def quebrar_linha(self, qtde_linhas=0):

    if not self.tampar:
      for i in range(qtde_linhas):
        print('')


c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

c1.escrever('Olá, tudo bem?')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, tudo bem?')
c1.quebrar_linha(2)
c2.escrever('Olá, gafanhoto! ')
c3.escrever('Vamos exercitar!')