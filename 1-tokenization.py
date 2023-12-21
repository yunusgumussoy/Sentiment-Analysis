# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:22:28 2023

@author: Yunus
"""

import nltk
nltk.download('punkt')
sentence = """Today I went for shopping"""
tokens = nltk.word_tokenize(sentence)

# print tokens
print(tokens)
