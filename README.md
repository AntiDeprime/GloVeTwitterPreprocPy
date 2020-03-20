[![Python Version](https://img.shields.io/badge/python-%3E%3D%203.6-blue)](https://github.com/AntiDeprime/GloVeTwitterPreprocPy/)
[![GitHub license](https://img.shields.io/github/license/AntiDeprime/GloVeTwitterPreprocPy)](https://github.com/AntiDeprime/GloVeTwitterPreprocPy/blob/master/LICENSE)

# GloVeTwitterPreprocPy
Python package for preprocessing Twitter data for [GloVe](https://nlp.stanford.edu/projects/glove/).

Based on original Ruby script: https://nlp.stanford.edu/projects/glove/preprocess-twitter.rb

## Installation 
```shell
pip install git+https://github.com/AntiDeprime/GloVeTwitterPreprocPy.git
```

## Usage

```python
from GloVePreprocessor import GloVePreprocessor

glove = GloVePreprocessor(lowercase=True)

glove.preprocess("Hello, @username! :) #one #two #three")
>> "hello, <user> ! <smile> <hashtag> one <hashtag> two <hashtag> three"

```
