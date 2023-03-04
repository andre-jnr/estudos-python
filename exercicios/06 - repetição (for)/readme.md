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

# Exercicios

- [Exercício 046:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/046_contagem_regressiva>) Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

- [Exercício 047:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/047_pares_de_1_ate_50>) Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

- [Exercício 048:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/048_soma_impares_multiloes_3>) Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

- [Exercício 049:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/049_tabuada_for>) Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

- [Exercício 050:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/050_soma_pares>) Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

- [Exercício 051:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/051_progressao_aritmetica>) Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

- [Exercício 052:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/052_numeros_primos>) Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

- [Exercício 053:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/053_derector_palindromo>) Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

  - APOS A SOPA

  - A SACADA DA CASA

  - A TORRE DA DERROTA

  - O LOBO AMA O BOLO

  - ANOTARAM A DATA DA MARATONA.

- [Exercício 054:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/054_grupo_maioridade>) Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

- [Exercício 055:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/055_maior_menor_sequencia>) Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

- [Exercício 056:](<https://github.com/andre-jnr/estudos-python/tree/main/exercicios/06%20-%20repeti%C3%A7%C3%A3o%20(for)/exercicios/056_analisador_completo>) Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
