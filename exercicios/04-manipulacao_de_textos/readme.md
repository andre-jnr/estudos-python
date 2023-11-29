# Manipulação de textos

- **String:** variável do tipo caractere (texto)
  > Uma string é qualquer texto escrito dentro de aspas
  > <br>

```python
# Como declarar e imprimir uma string:
minha_string = "qualquer texto"
print(f"Concatenar {minha_string} em string")
# Resultado: Concatenar qualquer texto em string
```

## Manipulação de strings

```python
# Todos os exemplos partem da premissa que declaramos essa variável:
minha_string = "qualquer texto"
```

### Manipulação de "tamanho"

- `minha_string.upper` -> transforma a string em maiúsculo
- `minha_string.lower()` -> transforma a string em minúsculo
- `minha_string.capitaliza()` -> deixa a primeira em maiúsculo e o resto em minúsculo

### Verifica o formato

- `minha_string.isupper()` -> verifica se a variável é maiúsculo
- `minha_string.islower()` -> verifica se a variável é minúsculo
- `minha_string.iscapitaliza()` -> verifica se a variável está capitalizada

### Úteis

- `minha_string.strip()` -> remove espaços desnecessários
- `len(minha_string)` -> conta quantos caractere

### Replace() -> substitui um caractere por outro

- `minha_string.replace("qualquer","meu")` -> meu texto
- `minha_string.replace("u","U")` -> qUalqUer texto
- `minha_string.replace("u","U", 1)` -> qUalquer texto (substitui só 1)

### Manipulação com índice

- `minha_string.index("u")` -> retorna o índice do u
- `minha_string.index("quer")` -> retorna o primeiro índice da palavra
- `minha_string[3]` -> retorna o segundo caractere
- `minha_string[0]` -> retorna o primeiro caractere
- `minha_string[2:5]` -> retorna do terceiro caractere até o 2° (não considera o último parâmetro)
- `minha_string[-1]` -> para retornar um caractere começando da esquerda (-1 seria o primeiro caractere da esquerda, ou o última da string)

<hr>

## Mais algumas informações

```python
# Para saber se o algum texto existe numa string
minha_string = "qualquer texto"
x = "texto" in minha_string
print(x)
# Resultado: True
```

> Lembrando que toda string é uma variavel composta de letras, então é possível percorrer cada letra:

```python
for letra in minha_string:
   print(letra)
```

## Impressão de strings

### Centralizar

- **Dois pontos(:):** informa que vamos tratar a variável
- **Circunflexo(^):** informa que queremos centralizar
- **N°:** informamos a quantidade de espaços onde será centralizado

```python
print(f'{"LISTAGEM DE PREÇOS":^30}')
```

### À esquerda

- **Dois pontos(:):** informa que vamos tratar a variável
- "**.**": informa que iremos preencher os espaço com pontos(.)
- **Menor que(<):** informa que que queremos centralizado a esquerda

```python
print(f'{listagem[produto]:.<20}')
```

### À direita

- **Dois pontos(:):** informa que vamos tratar a variável
- **Maior que(>):** informa que queremos centralizar à direita
- **.2f**: informa que queremos apenas 2 pontos flutuantes da variável

```python
print(f'R${listagem[produto]:>7.2f}')
```

# Exercicios

- [Exercício 022:](/exercicios/04-manipulacao_de_textos/exercicios/022_analisando_texto/022_analisador_texto.py) Crie um programa que leia o nome completo de uma pessoa e mostre:

  - O nome com todas as letras maiúsculas e minúscula.

  - Quantas letras ao todo (sem considerar espaços).

  - Quantas letras tem o primeiro nome.

- [Exercício 023:](/exercicios/04-manipulacao_de_textos/exercicios/023_separando_digitos/023_separador_digitos.py) Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

- [Exercício 024:](/exercicios/04-manipulacao_de_textos/exercicios/024_verificando_primeiras_letras_texto/024_verificador_primeira_letra_texto.py) Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

- [Exercício 025:](/exercicios/04-manipulacao_de_textos/exercicios/025_procurando_string_dentro_string/025_pessoa_silva_no_nome.py) Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

- [Exercício 026:](/exercicios/04-manipulacao_de_textos/exercicios/026_primeira_ultima_ocorrencia_string/026_quantos_a.py) Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

- [Exercício 027:](/exercicios/04-manipulacao_de_textos/exercicios/027_primeiro_ultimo_nome/027_primero_ultimo_nome.py) Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.