# Laço de repetição

Laço de repetição é um controle de fluxos que permite que um bloco de código seja executado repetidamente com base em uma determinada condição.

# While

O while é executado até que uma determinada condição seja verdadeira.

No exemplo a seguir, veremos um loop de 0 até 5, que em for seria `for i in range(0, 6):`

```mermaid
  graph TB;
      A([Inicio]) --> B[variavel = 0];
      B --> C{variavel < 5};
      C -->|verdadeiro| D[variavel + 1];
      D --> C;
      C -->|falso| E['variavel'];
      E --> F([Fim])
```

Em código ficaria assim:

```python
numero = 5
while numero < 5:
    numero += 1
print(numero)
```

Enquanto a condição for verdadeira, o laço continua. Então se você quiser criar um loop infinito, basta declarar o `while` como `True`,
e utilizar o `break` para _quebrar_ o loop: 

```python
while True:
    break
```

Podemos utilizar o `while` para validar entradas de dados, criando um loop infinito, para quebrar apenas quando a condição for validada.

```python
while True:
    numero = int(input( 'Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20
        break
    print('Tente novamente :(')
```
