# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 21:29:38 2018

@author: Arafat
"""

# stemming is mainly a data preproccessing technique
# It is used to stem a word
# such as: Writing will be stemmed to Write
# NLP has the stemming algorithm named 'Porter Stemmer' from 1979

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

words = ["writing", "written", "riding", "pythoning"]

ps = PorterStemmer()

for i in words:
    print(ps.stem(i))