# O básico - primeiros passos

Aqui, listarei tudo o que é necessário para tomar os primerios passos, nessa caminhada na programação em Python.

```python
print("Olá mundo!") # Imprime Olá mundo na tela.
```
<br/>

>❗ Toda variável do tipo String precisa conter ‘aspas simples’ ou “duplas”

<br/>

~~~python
type(variavel) # revela o tipo da variável.
print(type(variavel)) # Imprime na tela o tipo da variável
~~~

<br>

>❗ Para ler um número do usuário, utilizamos o comando `input`

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

var | tipo | exemplo
----|------|--------
string | caracter | '@andre2'
int | inteiros | -1, 0, 1
float | reais | 1.0, 1,2, 0,42

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

- [Exercício 001](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/01%20-%20Primeiros%20passos/exercicios/001_deixando_tudo_pronto): Declare uma variável que contenha o seu nome, e imprima na tela para o usuário.
- [Exercício 002](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/01%20-%20Primeiros%20passos/exercicios/002_respondendo_ao_usuario): Cria um programa que leia um valor qualquer, digitado pelo usuário, depois mostre: 
    - O tipo primitivo
    - Se só foi digitado espaços
    - Se é um número
