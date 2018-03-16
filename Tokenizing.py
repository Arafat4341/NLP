# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 01:37:29 2018

@author: Arafat
"""

from nltk.tokenize import sent_tokenize, word_tokenize

#Tokenizing is mainly separating text into words or sentences
# tokenizing : Word Tokenizer, Sentence Tokenizer
#corpora - body of text
#lexicons - words and their meaning
#lexicons are important to specify the meaning of the word
#business speak - "bull" means someone who is positive in market
#normal english - "bull" means an animal

sentence = "Hey Mr. X! How are you this morning? I heard you fell sick since last night"
print(sent_tokenize(sentence))
print(word_tokenize(sentence))
