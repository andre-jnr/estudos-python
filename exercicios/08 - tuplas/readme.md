# Tuplas

São coleções de dados imutáveis, lista inalteradas.

Há dois meios para criar tuplas:

```python
tupla = ("exemplo1", "Exemplos2", "Exemplos3")
tupla = "exemplo1", "Exemplos2", "Exemplos3"
```

> A fragmentação das tuplas funcionam semelhante a [lista](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/09%20-%20listas).

## Repetições em tuplas

Percorrer uma tupla

```python
lanche = ('Pizza', 'Pudim', 'Bolacha')
for comida in lache:
    print(f'Eu comi {comida}')
print('Comi pra caramba!')

# Eu comi Pizza
# Eu comi Pudim
# Eu comi Bolacha
# comi pra caramba!
```

```python
lanche = ('Pizza', 'Pudim', 'Bolacha')
for contador in range(0, len(lanche)):
    print(f'Eu comi {lanche[contador]}')
  
# Eu comi Pizza
# Eu comi Pudim
# Eu comi Bolacha
```

Imprimir o indice e o item da tupla:

```python
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
```

## Algumas funções úteis

- `tupla.count(elemento)`: retorna a quantidade de vezes em que `elemento` aparece na lista.
- `tupla.index(elemento)`: retorna o índice/ posição do `elemento`.
- `del(tupla)`: deleta a tupla.
- `print(sorted(tupla))`: imprime a `tupla` em ordem crescente(números) ou alfabetica(`string`), mas apenas podemos imprime,
pois as `tuplas` são imutáveis.

Podemos criar uma `tupla` com dados de outras tuplas:

```python
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
```
