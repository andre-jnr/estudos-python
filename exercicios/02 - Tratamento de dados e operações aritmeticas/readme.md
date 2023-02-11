# Tratamento de dados e operações aritméticas

#  Int e Float - variáveis do tipo inteiro e real

**Variáveis do tipo inteiro (int):** são os números positivos e negativos, que não apresentam parte decimal e, o zero.

- …-1, 0, 2…

**Variáveis do tipo real (float):** são quaisquer números inteiros ou decimais.

- …-1,-1,5, 0, 1, 1,5…
    
>    N1 = 5 <br>
>     ‣ 5 é um variável do tipo int
>    
>    N2 = 5.5 <br>
>     ‣ 5.5 é uma variável do tipo float

**Para declara uma variável do tipo float:**

```python
N3 = float(5)
Print(n3)

# Resultado: 5.0
```

Para transformar uma variável para outro tipo, é necessário criar uma nova variável:

```python
n1 = 5
a = float(n1)
```
```python
# Ou você pode simplesmente substrituir a mesma variável
n1 = 5
n1 = float(n1)
```

# Matemática
No python, conseguimos realizar operações aritméticas, e comparações lógicas.

## Operadores aritméticos

A tabela abaixo mostra o grau de prioridade, quando maior o número, maior será a prioridade,
ou seja, será a operação realizada por primerio.

Prioridade | símbolo | significado
-----------|---------|------------
4 | ( ) | prioridade
1 | + | adição
1 | - | subtração
2 | * | multiplicação
2 | / | divisão
2 | % | modulo
2 | // | divisão inteira
3 | ** | potencialização

## Comparadores lógicos (booleanos)

símbolo | significado
---------|------------
\> | Maior que...
=> | Maior ou igual a...
== | Igual a...
!= | Diferente...
< | Menor que...
=< | Igual ou menor que...

> 📌 Valores booleanos sempre retornam True ou False

> 📌 Se usado os comparadores de Maior e Menor (</>) com `strings`, retornará de acordo com ordem alfabética.

Para comparar o tamanho de um texto com outro, usamos a função `len()`:
```python
variavel1 = 'círculo'
variavel2 = 'paralelepípedo'
len(variavel1) > len(variavel 2)
```

## Funções

- `abs(n)`: retorna o absoluto de `n`.
- `pow(n, v)`: retorna a exponenciação de `n` elevado a `v`.
- `max(n, a, b...)`: retorna o **maior** valor da cadeia.
- `min(n, a, b...)`: retorna o **menor** valor da cadeia.
- `round(n)`: retorna para **arredondamento** mais próximo.
- `variavel.count(n)`: retorna a quantidade de vezes de `n` dentro da variavel.

## Biblioteca de matemática
Biblioteca é são um conjunto de função, e nem todas as funções estão disponíveis nativamente
no Python, para usar esses recursos, importamos a biblioteca.
```python
import math # Para importar
```
- `math.floor(n)`: retorna o arredondamento de `n` para baixo.
- `math.ceil(n)`: retorna o arredondamento de `n` pra cima.
- `math.sqrt(n)`: retorn a raiz quadrada de `n`.
- `cos(x)`: retorna o valor cosseno de `x` radianos.
- `sin(x)`: retorna o valor do seno de `x` radianos.
- `tan(x)`: valor da tangente de `x` radianos.

Se você não quiser importar toda a biblioteca, você pode importar só a função que vai utilizar.
```python
from math import floor
# Importa só a função floor
```
- `floor(n)`: retorna o arredondamento de `n` para baixo.
