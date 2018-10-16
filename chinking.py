# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:13:07 2018

@author: Arafat
"""
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

"""
Chinking fro, chunking is removal of something. Such as: we can remove
 verbs etc.

"""


train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text) #A

tokenized = custom_sent_tokenizer.tokenize(sample_text)   #B

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""chunk: {<.*>+}
                                    }<VB.?|IN|DT|VBN>+{"""
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            print(chunked)
            
            
            
            
            #print(tagged,'\n')
    
    except Exception as e:
        print(str(e))


process_content()