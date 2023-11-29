# Bibliotecas - modulos

Uma biblioteca é uma coleção de recursos que podem ser importados para serem usados.
Quando importamos um modulo, temos acesso a várias funções criadas por outros desenvolvedores.

Pra instalar algum modulo não nativo:

```powershell
pip install modulo
```

Para importar uma biblioteca:

```python
import biblioteca
```

Para importar apenas uma função da biblioteca:

```python
from biblioteca import funcao
```

Podemos importar mais de uma função por vez

```python
from biblioteca import funcao1, funcao2
```

lembrando que podemos renomear tanto os modulos, como suas respectivas funções:

```python
import biblioteca as bb
from biblioteca import funcao as fc
```

Para usar uma função de uma biblioteca:

```python
modulo.funcao(variavel)
```

Se caso, você tenha importado só a função:

```python
funcao(variavel)

```

# Bibliotecas populares

## Bibliotecas nativas

- math
- random
- datetime

## Desenvolvimento web

- Django
- Flask
- Tornado
- Web2Py
- CherryPy
- Bottle
- TurboGears

## Segurança da informação

- URLLib
- Requests
- Socket
- HTTPLib
- PyAesCrypt

## Ciência de dados

- Scikit learn
- NumPy
- SciPy
- Numba
- TensorFlow
- PyTorch
- Keras
- NLTK
- SpaCy
- Gensim
- Scrapy
- Beautiful Soup
- Requests
- PyOD
- QGrid
- LightGBM
- Vaex
- XGBoost
- CatBoost
- Matplotlib
- Pandas
- Plotly
- LIME
- Featuretools
- StatsModels
- Seaborn
- Bokeh
- Pydot

## Bioinformática

- DB-API
- Pillow
- NumPy
- HTMLgen
- PyGTK
- WxPython

## Estatística

- RPy
- Scipy
- PyChem

## Processamento de Imagens

- Pillow
- OpenCV
- Scikit-image
- SciPy
- NumPy

# Exercicios

- [Exercício 016:](/exercicios/03-modulos/exercicios/016_quebrando_numero/016_arrendondando_numero.py) Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

- [Exercício 017:](/exercicios/03-modulos/exercicios/017_catetos_hipotenusa/017_cateto_hipotenusa.py) Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

- [Exercício 018:](/exercicios/03-modulos/exercicios/018_trigonometria/018_seno_cosseno_tangente.py) Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

- [Exercício 019:](/exercicios/03-modulos/exercicios/019_sorteando_itens_lista/019_sorteando_item_lista.py) Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

- [Exercício 020:](/exercicios/03-modulos/exercicios/020_sorteando_ordem_lista/020_sorteando_ordem_lista.py) O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

- [Exercício 021:](/exercicios/03-modulos/exercicios/021_trocando_mp3/021_tocando_mp3.py) Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.