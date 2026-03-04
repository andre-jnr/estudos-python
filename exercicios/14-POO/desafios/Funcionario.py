class Funcionario:
  def __init__(self, nome, setor, cargo, aposentado=False):
    self.nome = nome
    self.setor = setor
    self.cargo = cargo


  def aposentar(self):
    self.aposentado = True


  def apresentacao(self):
    return f'🤝Olá, sou {self.nome}, sou {self.cargo} do setor de {self.cargo} da empresa Curso em Video!'