# Lista

Em Python, uma lista é uma estrutura de dados que permite armazenar uma coleção de itens em uma única variável. As listas são mutáveis, o que significa que podem ser modificadas após serem criadas.

Uma lista é representada por uma sequência de objetos separados por vírgula e dentro de colchetes [], assim, uma lista vazia, por exemplo, pode ser representada por colchetes sem nenhum conteúdo.

<hr>

Há dois meios para criar uma lista vazia:

```python
lista = []
lista = list()
```

> É possível pôr listas dentro de listas:

```python
lista1 = [10, "junior", [20, "Andre"]]
lista2 = ["qualquer coisa", lista1]
```

Se você declarar um novo elemento em um índice que já há alguma coisas, o elemento anterior será substituído pela novo elemento.

```python
lanche = ['hamburguer', 'refri', 'pizza', 'pudim']
lanche[3] = 'picolé'

# lanche = ['hamburguer', 'refri', 'pizza', 'picolé']
```

## Métodos úteis

Para adicionar um novo item a lista (ficará na última posição):

```python
lista.append(item)
```

Para adicionar e escolher o índice do item:

```python
lista.insert(2, item)

# Todos os itens da lista permanecem
# No índice 2 é adionado o item, e o restante é empurrado pra frente
```

Para adicionar os itens de uma lista em outra:

```python
lista.extend(lista2)
```

Para remover itens de uma lista.

```python
lista.pop() # Remove o último item da lista
lista.pop(0) # Remove o item especificado pelo index
```

Para remover o item pelo nome(valor):

```python
lista.remove(item) #remove o primeiro valor com esse nome
```

Retorna a quantidade de vezes que o item está na lista:

```python
lista.count(item)
```

Para organizar a lista de forma crescente:

```python
lista.sort()
```

Para organizar a lista de forma decrescente:

```python
lista.sort(reverse=True)
```

Para saber o tamanho da lista (quantos itens há nela):

```python
len(lista)
```

Para somar todos os elementos da lista:

```python
sum(lista)
```

Retorna o maior item da lista:

```python
max(lista)
```

Retorna o menor item da lista:

```python
min(lista)
```

Reverter os elementos da lista:

```python
list.reverse()
```

Retorna uma lista com a cópia dos elementos da lista de origem:

```python
list.copy()
```

## Algoritmos úteis

Para testar se o valor existe antes de apagar:

```python
if 'pizza' in lanche:
	lanche.remove('pizza')
```

Para criar uma lista com uma faixa de números:

```python
valores = list(range(4, 11))

# valores = [4, 5, 6, 7, 8, 9, 10]
```

Para ordenar uma lista:

```python
ordem = [2, 5, 3, 9, 10, 100, 54, 75, 44]
ordem.sort()
print(ordem)

# output
# 2, 3, 5, 9, 10, 44, 54, 75, 100
```

Para saber se o elemento existe na lista:

```python
if elemento in lista:
	print('Existe!')
```

```python
if lista.index(elemento) == True:
	print('Existe')
else:
	print('Não existe')
```

Para percorrer cada item da lista:

```python
for item in lista:
	print(item)
```

Para percorrer cada item e índice da lista:

```python
for indice, elemento in enumerate(lista):
	print(f"Na posição {indice} encontrei o valor {elemento}!")
```

Para o usuário inserir 5 valores:

```python
lista = list()
for i in range(0, 5):
	valores.append(int(input("Digite um valor: ")))
```

Para fazer uma ligação entre listas (tudo o que for realizado numa, será realizado na outra):

```python
min(lista)a = [1, 2, 3, 5]
b = a
```

Para apenas copiar os itens de uma lista para outra:

```python
a = [1, 2, 3, 5]
b = a[:]
```

## Índices de listas

> `lista = [1, 2, 3, 4, 5]`
> values = 1, 2, 3, 4, 5
> index = 0, 1, 2, 3, 4

Retorna o índice do item

```python
lista.index(item)
```

Para imprimir o primeiro item da lista:

```python
print(lista[0])
```

Para imprimir o último item da lista:

```python
print(lista[-1])
```

Pegar do primeiro item até o último:

```python
lista[0:4]
```

Pega do segundo item até o último:

```python
lista[1:]
```

Pega do terceiro item até o quinto, pulando de 2 em 2:

```python
lista[2:6:2]
```

## Exercícios

[Exercício 078](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/09%20-%20listas/exercicios/078_posicao_maior): Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

[Exercício 079](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/09%20-%20listas/exercicios/079_valores_unicos_crescente): Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

[Exercício 080](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/09%20-%20listas/exercicios/080_valores_ordenados_sem_sort): Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o `sort()`). No final, mostre a lista ordenada na tela.

[Exercício 081](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/09%20-%20listas/exercicios/081_extraindo_dados_listas): Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

- Quantos números foram digitados.
- A lista de valores, ordenada de forma decrescente.
- Se o valor 5 foi digitado e está ou não na lista.

[Exercício 082](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/09%20-%20listas/exercicios/082_dividindo_valores_listas): Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

[Exercício 083](https://github.com/andre-jnr/estudos-python/tree/main/exercicios/09%20-%20listas/exercicios/083_validando_expressoes_matematicas): Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

- Quantas pessoas foram cadastradas.
- Uma listagem com as pessoas mais pesadas.
- Uma listagem com as pessoas mais leves.
