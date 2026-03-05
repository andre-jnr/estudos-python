from rich import print
from rich import inspect

class Funcionario:
  empresa = 'Curso em video'

  def __init__(self, nome, setor, cargo):
    self.nome = nome
    self.setor = setor
    self.cargo = cargo


  def apresentacao(self) -> str:
    return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do soter de {self.setor} da empresa {Funcionario.empresa}'
  

inspect(Funcionario)

f1 = Funcionario('Pedro', 'TI', 'Programador')
inspect(f1)

print(f1.apresentacao())