# Laço de repetição

Laço de repitação é um controle de fluxos que permite que o código seja executado repetidamente com base em uma determinada condição.

# For

Utilizamos quando sabemos a quantidade de repetições que um bloco de código deve ser executado.

O `for` cria uma variavel de controle, e é executado quantas vezes for determinado.

```python
for variavel in range(10):
    print(variavel)
  
# Resultado
  # 0
  # 1
  # 2
  # 3
  # 4
  # 5
  # 6
  # 7
  # 8
  # 9
```

Repetição numa faixa de 1 até 4

```python
for variavel in range(1, 5):
```

Repetição numa faixa de 1 até 9, de 2 em 2:

```python
for variavel in range(1, 10, 2):
    print(variavel)

# Resultado:
  # 1
  # 3
  # 5
  # 7
  # 9
```

Lembrando que você pode percorrer uma `string` ou uma lista:

```python
for variavel in lista:
    print(variavel)
```
