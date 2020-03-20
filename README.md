# GloVeTwitterPreprocPy
Python script for preprocessing Twitter data.

Based on original Ruby script: https://nlp.stanford.edu/projects/glove/preprocess-twitter.rb

## Installation 
`pip install git+https://github.com/AntiDeprime/GloVeTwitterPreprocPy.git`

## Usage

`from GloVePreprocessor import GloVePreprocessor` 

`glove = GloVePreprocessor(lowercase=True)`

`glove.preprocess('Hello, @username! :) #one #two #three ')`
`> 'hello, <user> ! <smile> <hashtag> one <hashtag> two <hashtag> three'`
