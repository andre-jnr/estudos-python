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
