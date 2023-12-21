# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 18:26:03 2023

@author: Yunus
"""

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
train = [('I like coffee', 'positive'),
         ('I am playing baseball', 'neutral'),
         ('I like natural language processing', 'positive'),
         ('This book is amazing', 'positive'),
         ('I cannot read the whole book at once', 'negative'),
         ('I was able to call you yesterday', 'neutral')    
]
cl=NaiveBayesClassifier(train)
cl.classify("I am happy"'positive')
blob=TextBlob("This movie is good", classifier=cl)
for s in blob.sentences:
    print(s)
    print(s.classify())