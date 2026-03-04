'''
Crie a classe ControleRemoto, onde vamos
simular o funcionamento de um controle
simples (canal, volume, liga/desliga)
'''
from rich import print
from rich.panel import Panel
from rich.traceback import install
import os

install()

class ControleRemoto:
  def __init__(self, tv_ligada=False):
    self.tv_ligada = tv_ligada
    self.canais = [' ' for i in range(1, 6)]
    self.faixa_volume = [' ' for i in range(0, 6)]
    self.canal = 1
    self.volume = 0


  def ligar_desligar(self):
    self.tv_ligada = not self.tv_ligada


  def voltar_canal(self):
    if self.canal == 1:
      self.canal = len(self.canais)
    else:
      self.canal -= 1

  def  avancar_canal(self):
    if self.canal == len(self.canais):
      self.canal = 1
    else:
      self.canal += 1

  
  def diminuir_volume(self):
    if self.volume == 0:
      self.volume = 0
    else:
      self.volume -= 1


  def aumentar_volume(self):
    if self.volume == len(self.faixa_volume):
      self.volume = self.volume
    else:
      self.volume += 1

  def acoes(self):
    try:
        usuario = str(input(''))

        if usuario == '@':
          self.ligar_desligar()
        else:
          match usuario:
            case '<':
              self.voltar_canal()
            case '>':
              self.avancar_canal()
            case '-':
              self.diminuir_volume()
            case '+':
              self.aumentar_volume()

        self.mostrarTV()
    
    except KeyboardInterrupt:
      self.mostrarTV()


  def mostrarTV(self):
    os.system('cls' if os.name == 'nt' else 'clear')

    titulo = ' [ TV ] '
    tamanho = 30

    canais = " ".join(
    f'[white on yellow] {i + 1} [/]' if i + 1 == self.canal 
    else f' {i + 1} '
    for i, _ in enumerate(self.canais)
)
    
    faixa_volume = "".join(
      f'[white on blue] [/]' if i < self.volume
      else f'[blue on white] [/]'
      for i, _ in enumerate(self.faixa_volume)
    )

    if self.tv_ligada:
      paniel = Panel(
        f'''CANAL = {canais}
VOLUME = {faixa_volume}''',
        title=titulo,
        width=tamanho
      )
    else:
      paniel = Panel(
        '[red]🚫 A TV está desligada [/]',
        title=titulo,
        width=tamanho
      )

    print(paniel)
    print(f'< CH{self.canal} >   - VOL{self.volume} +  ', end='')


TV = ControleRemoto()
while True:
  TV.mostrarTV()
  TV.acoes()