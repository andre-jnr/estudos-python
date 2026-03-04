class Produto:
  def __init__(self, descricao, preco):
    self.descricao = descricao
    self.preco = preco


  def etiqueta(self):
    from rich import print
    from rich.panel import Panel

    painel = Panel(
      f'{self.descricao:^30}\n{"":-^30}{f"R$ {self.preco:,.2f}":.^30}',
      title='Produto',
      width=35
      )
    
    print(painel)
    
produto1 = Produto('notebook gamer', 5_000)
produto1.etiqueta()