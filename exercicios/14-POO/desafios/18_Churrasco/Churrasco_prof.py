from rich import print
from rich.panel import Panel

class Churrasco:
  consumo_padrao:float = 0.400 # cada pessoa come em média 400g de carne
  preco_kg:float = 82.40 # Cada kg de carne custa R$ 82.40

  def __init__(self, titulo, qtde):
    self.titulo = titulo
    self.qtde = qtde


  def __str__(self):
    return f'Esse é {self.titulo} com {self.qtde} pessoas participando'
  

  def calcular_qtde_carne(self) -> float:
    return self.qtde * Churrasco.consumo_padrao


  def calcular_custo_total(self) -> float:
    return self.calcular_qtde_carne() * Churrasco.preco_kg


  def calcular_custo_individual(self) -> float:
    return self.calcular_custo_total() / self.qtde
  

  def analisar(self):

    conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.qtde} convidados[/]'
    conteudo += f'\nCada participante comerá {Churrasco.consumo_padrao}kg e cada Kg custa R${Churrasco.preco_kg:,.2f}'
    conteudo += f'\nRecomendo [blue]comprar {self.calcular_qtde_carne():,.2f}Kg[/] de carne'
    conteudo += f'\nO custo total será de R${self.calcular_custo_total():,.2f}'
    conteudo += f'\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/] para participar'

    painel = Panel(conteudo, title=self.titulo)
    print(painel)


churrasco = Churrasco('Churras dos amigos', 15)
churrasco.analisar()

churrasco2 = Churrasco('Festa de fim de ano', 80)
churrasco2.analisar()