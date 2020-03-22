#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Martin Kondra"

import nltk.corpus
from Corpus import corpus
from random import choice

#hacer que las funciones tengan un return, no que no sea "none"!

def generate_model(cfdist, word, num=15):
    autotext = ""
    for i in range(num):
        autotext += word + " "
        word = cfdist[word].max()
    return autotext


def another_model(cfdist, word, num=15):
    autotext = ""
    for i in range(num):
        autotext += word + " "
        wordlist = list(cfdist[word])
        #print wordlist
        word = choice(wordlist)
    return autotext

def poem(cfd, lines=10, num=10):
    for i in range(lines):
        word = choice(corpus.words("martinfierro.txt"))
        autotext = another_model(cfd, word, num)
        print autotext


text = corpus.words('martinfierro.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
autotext1 = generate_model(cfd, 'Cuando')
autotext2 = another_model(cfd,"Cuando")


if __name__ == "__main__":
    #print autotext2
    poem(cfd)

