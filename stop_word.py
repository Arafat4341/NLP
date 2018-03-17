# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 01:42:40 2018

@author: Arafat
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Stop words are the words we don't care that much about.
#In other words we just want to eliminate them from out sentences
#they may be useful to us to make sense but in data analysis, they may be useless

example_sentence = "This is an example sentence showing off the stop wordfilterization"

#Stop words default list in English
stop_words = set(stopwords.words("english"))

#print(stop_words)

words = word_tokenize(example_sentence)
filtered_words = []

"""for w in words:
    if not w in stop_words:
        filtered_words.append(w)"""

filtered_words = [w for w in words if not w in stop_words]
print(filtered_words)

