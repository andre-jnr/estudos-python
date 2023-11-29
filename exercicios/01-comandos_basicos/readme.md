# Comandos básicos

Aqui, listarei tudo o que é necessário para tomar os primerios passos, nessa caminhada na programação em Python.

```python
print("Olá mundo!") # Imprime Olá mundo na tela.
```

<br/>

> ❗ Toda variável do tipo String precisa conter ‘aspas simples’ ou “duplas”

<br/>

```python
type(variavel) # revela o tipo da variável.
print(type(variavel)) # Imprime na tela o tipo da variável
```

<br>

> ❗ Para ler um número do usuário, utilizamos o comando `input`

<br>

```python
variavel_de_entrada = input('Digite um valor: ')
```

<br>

## Variáveis

- Variáveis são espaços na memória da máquina, dedicados à algum dado.
- No python as variáveis são atribuídas pelo sinais de igual(=)

```python
variavel = 10
```

<br>

### Tipos de variaveis

Há 4 tipos de variáveis

| var    | tipo     | exemplo        |
| ------ | -------- | -------------- |
| string | caracter | '@andre2'      |
| int    | inteiros | -1, 0, 1       |
| float  | reais    | 1.0, 1,2, 0,42 |

<br>

### Primeiros passos

- Para declarar uma variável do tipo string, utilizamos aspas simples ou duplas:

```python
nome = "Júnior"
print(f"Meu nome é {nome}")

# O resultado será: Meu nome é Júnior
```

<br>

- Também é possível separar o texto da variável utilizando vírgula:

```python
nome = 'junior'
print('meu nome é ', nome)

# O resultado será: meu nome é junior
```

<br>

- Exemplos de um código utilizando vários tipos de variáveis

```python
nome = 'Júnior'
idade = 24
gosto = 'ler'

print(f"Meu nome é {nome}" )
print(f"Eu gosto de {gosto}" )
print(f"Eu tenho {idade} anos")
print(f"{nome} gosta de {gosto}, e tem {idade} anos")
```

<br>

- O python interpreta linha por linha, então é possível mudar uma variável já declarada

```python
nome = "Júnior"
idade = "24"
gosto = "ler"

print(f"Meu nome é {nome}" )
print(f"Eu gosto de {gosto}" )

idade = "19"

print(f"Eu tenho {idade} anos")
print(f"{nome} gosta de {gosto} e tem {idade} anos")
```

### Exercícios

Agora você tem o necessário para tomar os primeiros passos em python!

- [Exercício 01:](/exercicios/01-comandos_basicos/exercicios/001_deixando_tudo_pronto/) Declare uma variavel com o nome do programador e exiba ela ao usuário.

- [Exercício 002:](/exercicios/01-comandos_basicos/exercicios/002_boas-vindas/002_boas-vindas.py) Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

- [Exercício 003:](/exercicios/01-comandos_basicos/exercicios/003_soma/003_soma.py) Crie um programa que leia dois números e mostre a soma entre eles.

- [Exercício 004:](/exercicios/01-comandos_basicos/exercicios/004_tipo_primiticos/004_revelando_tipo_primitivo.py) faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo, e todas as informações possíveis sobre ela.