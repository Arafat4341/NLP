# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 23:19:35 2018

@author: Arafat
"""


import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


"""
The main objective of using chunks is to better understand the sentence. 
Who the sentence is talking to. There may be multiple nouns in a sentense. 
We can find exactly which noun the sentence is talking about by dividing the
sentence into chunks and have a more precise understanding.


Chunking is also called shallow parsing and it's basically the identification
of parts of speech and short phrases (like noun phrases). Part of speech
tagging tells you whether words are nouns, verbs, adjectives, etc, but it 
doesn't give you any clue about the structure of the sentence or phrases in 
the sentence. Sometimes it's useful to have more information than just the 
parts of speech of words, 
but you don't need the full parse tree that you would get from parsing.

"""

"""
POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
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
            chunkGram = r"""chunk: {<RB.?>*<VB.?>*<NNP>+<NN>}"""
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            print(chunked)
            
            
            
            
            #print(tagged,'\n')
    
    except Exception as e:
        print(str(e))


process_content()
