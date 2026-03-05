from rich import print
from rich.panel import Panel


class Produto:
  def __init__(self, descricao, preco):
    self.descricao = descricao
    self.preco = preco


  def __str__(self):
    return f'{self.descricao} custa R${self.preco:,.2f}'
  

  def etiqueta(self):

    conteudo = f"{self.descricao.center(30, ' ')}"
    conteudo += f"{'-' * 30}"
    conteudo += f"R${self.preco:,.2f}".center(30, '.')

    etiqueta = Panel(conteudo, title='Produto', width=34)
    print(etiqueta)


p1 = Produto('Iphone 17 Pro Max', 25_000.85)
print(p1)
p1.etiqueta()