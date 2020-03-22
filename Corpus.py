#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Martin Kondra"


import os
from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text

corpus = PlaintextCorpusReader(os.getcwd(), "[a-zA-Z0-9]*.txt")

text1 = corpus.fileids()[0].decode("utf-8")

words = corpus.words(text1)
sents = corpus.sents(text1)

facundo = Text(corpus.words(text1))

if __name__ == "__main__":
    print corpus.fileids()
    print words[1000:1050]
    print sents[100:110]
    facundo.concordance("salvaje")
