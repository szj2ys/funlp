
<p align="center">
    <img width="200" src="https://github.com/szj2ys/funlp/raw/master/datasets/resources/logo.png"/>
</p>

<h3 align="center">
    <p>Having fun with language processing</p>
</h3>


<p align="center">
    <a href="https://python.org/pypi/funlp">
        <img src="https://badge.fury.io/py/funlp.svg" alt="Version"/>
    </a>
    <a href="https://python.org/pypi/funlp">
        <img src="https://img.shields.io/pypi/l/funlp.svg?color=orange" alt="License"/>
    </a>
    <a href="https://python.org/pypi/funlp">
        <img src="https://img.shields.io/pypi/dm/funlp?color=blue" alt="pypi downloads"/>
    </a>
    <a href="https://python.org/pypi/funlp">
        <img src="https://img.shields.io/github/last-commit/szj2ys/funlp?color=blue" alt="GitHub last commit"/>
    </a>
    <a href="https://github.com/szj2ys/funlp">
        <img src="https://img.shields.io/github/stars/szj2ys/funlp?style=social" alt="Stars"/>
    </a>
</p>




# Installation
```shell
pip install funlp
```
you may want to checkout the version
```shell
funlp version
```
Haha, `funlp` is now on your environment, having fun with it, enjoy ...


# Usage
## TextRank4Sentence
```python
from funlp import TextRank4Sentence
import codecs

rank4sent = TextRank4Sentence(use_w2v=False,tol=0.0001)

text = codecs.open('./datasets/input/当前中国经济实现完全数字化，小微企业的投资机会将是蓝海.txt', 'r', 'utf-8').read()
rank4sent.summarize(text, 10)
```

## 
```python
from funlp import TextRank4Words
import codecs

rank4words = TextRank4Words(tol=0.0001,window=2)

text = codecs.open('../datasets/input/当前中国经济实现完全数字化，小微企业的投资机会将是蓝海.txt', 'r', 'utf-8').read()
rank4words.summarize(text, 10)
```

## Acknowlegements
*   The project is largely based on [FastTextRank](https://github.com/ArtistScript/FastTextRank)
*   Code implementation is inspired by [Fasttext](https://github.com/facebookresearch/torchbeast)

