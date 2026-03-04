'''
Crie a classe Gamer, onde podemos cadastrar
nome, nick e os jogos favoritos de uma pessoa.
Crie também um método que permita mostrar a ficha
desse gamer
'''
from rich import print
from rich.panel import Panel

class Gamer:
  def __init__(self, nome, nick, lista_jogos=[]):
    self.nome = nome
    self.nick = nick
    self.lista_jogos = lista_jogos


  def add_favoritos(self, jogo):
    self.lista_jogos.append(jogo)


  def ficha(self):
    jogos_formatados = "\n".join(
        f"🎮 {jogo}" for jogo in self.lista_jogos
    )
    paniel = Panel(
      f'''Nome real: [black on blue]{self.nome}[/]
Jogos favoritos:
[blue]{jogos_formatados}[/]''',
      title=f'Jogador <{self.nick}>'
    )

    print(paniel)


player1 = Gamer('andre', 'proxy')
player1.add_favoritos('God of wars')
player1.add_favoritos('Resident Evil 4')
player1.add_favoritos('Valorant')
player1.ficha()