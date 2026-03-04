from rich import print
'''
Crie a classe Livro, que vai simular
a passagem de páginas de um livro,
considerando também se o usuário chegou
ao fim da leitura
'''
class Livro:
  def __init__(self, titulo='', qtde_paginas=0):
    self.titulo = titulo
    self.qtde_paginas = qtde_paginas
    self.pagina_atual = 1
    print(f'[blue]📖 Você acabou de abrir o livro \'[red]{self.titulo}[/]\' que tem [green]{self.qtde_paginas} páginas[/] no total. Você agora está na[/] [yellow]página {self.pagina_atual}[/]')

  
  def avancar_paginas(self, paginas_para_avancar=1):
    nova_pagina = min(
            self.pagina_atual + paginas_para_avancar,
            self.qtde_paginas
        )
    
    paginas_realmente_avancadas = nova_pagina - self.pagina_atual

    for i in range(self.pagina_atual + 1, nova_pagina):
      print(f'Pág{i} ', end='▶️  ')
    
    self.pagina_atual = nova_pagina

    print(f'[blue]Você avançou {paginas_realmente_avancadas} e agora está na[/] [yellow]página {self.pagina_atual}[/]')

    if self.pagina_atual == self.qtde_paginas:
      print(f'[red]📕 Você chegou ao final do livro \'{self.titulo}\'[red]')


livro1 = Livro('10 coisas que aprendi', qtde_paginas=20)
livro1.avancar_paginas(5)
livro1.avancar_paginas(10)
livro1.avancar_paginas(100)