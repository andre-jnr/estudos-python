class Gafanhoto:
  '''
    Essa classe cria um  gafanhoto, que é uma pessoa que tem nome e idade
    Para criar um nome pessoa, use
    variavel = Gafanhoto(nome, idade)
  '''
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def aniversario(self):
    self.idade += 1
  
  def __str__(self):
    return f'{self.nome} tem {self.idade:.0f} anos'

eu = Gafanhoto('Andre', 20)
print(eu)
eu.aniversario()
print(eu)
print(eu.__dict__)
print(eu.__getstate__())
print(eu.__class__)