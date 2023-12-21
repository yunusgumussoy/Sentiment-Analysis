# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:22:28 2023

@author: Yunus
"""

"pip install textblob "     #for installation

import textblob            #to import

from textblob import TextBlob
blob = TextBlob ("Yunus is bright and attentive and produces good-quality written academic work")
print(blob.sentiment)

# Polarity refers to how positive or negative a text is, while subjectivity refers to how opinionated or factual a text is


# Text correction
text = "Yunus is brigh and attntive and prodces good-qualty writtn academc wrk"
output = TextBlob(text).correct()
print(output)
