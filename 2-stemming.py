# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:22:28 2023

@author: Yunus
"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
words = ["gaming", "games", "game"]

for w in words:
    stemmed_word = ps.stem(w)
    print(f"{w} : {stemmed_word}")


