# Tuplas

São coleções de dados imutáveis, listas inalteradas.

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

## Funções e métodos úteis

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

# Exercicios

- [Exercício 072:](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/08%20-%20tuplas/exercicios/072_tuplas_times_futebol) Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

- [Exercício 073:](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/08%20-%20tuplas/exercicios/073_numeros_por_extensos) Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

  - Os 5 primeiros times.

  - Os últimos 4 colocados.

  - Times em ordem alfabética.

  - Em que posição está o time da Chapecoense.

- [Exercício 074:](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/08%20-%20tuplas/exercicios/074_maior_menor_tupla) Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

- [Exercício 075:](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/08%20-%20tuplas/exercicios/075_analise_dados_tupla) Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

  - Quantas vezes apareceu o valor 9.

  - Em que posição foi digitado o primeiro valor 3.

  - Quais foram os números pares.

- [Exercício 076:](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/08%20-%20tuplas/exercicios/076_listagem_precos_tupla) Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

- [Exercício 077:](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/08%20-%20tuplas/exercicios/077_contador_de_vogais) Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
