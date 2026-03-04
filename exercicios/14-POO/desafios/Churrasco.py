from rich import print
from rich.panel import Panel

class Churrasco:
  '''
  Cria a classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco a o preço por pessoa.

  Considere
  consumo padrão: 400g por pessoa
  Preço: R$82,40/kg
  '''
  def __init__(self, titulo='',
               qtde_pessoas=0,
               preco_carne=82.40,
               consumo_medio=0.40):
    self.titulo = titulo
    self.qtde_pessoas = qtde_pessoas
    self.preco_carne = preco_carne
    self.consumo_medio = consumo_medio


  def consumo_total(self):
    return self.qtde_pessoas * self.consumo_medio
  

  def custo_total(self):
    return self.preco_carne * self.consumo_total()

  def preco_por_pessoa(self):
    if self.qtde_pessoas <= 0:
      raise ValueError("A quantidade de pessoas deve ser maior que zero.")
    return self.custo_total() / self.qtde_pessoas


  def analisar(self):
    '''
    Acho que deveria ser um __str__,
    mas vou fazer igual o professor mostrou no exemplo
    '''

    painel = Panel(
      f'''Analisando [green]{self.titulo}[/] com [blue]{self.qtde_pessoas} convidados[/]
Cada particiopante comerá {self.consumo_medio:.1f}kg e cada Kg custa R${self.preco_carne:.2f}
Recomendo [blue]comprar {self.consumo_total():.3f}kg[/] de carne
O custo total será de [green]R${self.custo_total():.2f}[/]
Cada pessoa pagará [yellow]R${self.preco_por_pessoa():.2f}[/] para participar.
      '''
    )

    print(painel)

churrasco = Churrasco('Churras dos Amigos', qtde_pessoas=15)
churrasco.analisar()
  