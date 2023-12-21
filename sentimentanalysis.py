# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:52:34 2023

@author: Yunus
"""

import nltk
nltk.download('vader_lexicon')
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
#╦from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Benjamin Netanyahu's speech, Oct 10th, 2023
speech = "Israel is at war. We didn't want this war. It was forced upon us in the most brutal and savage way. But though Israel didn't start this war, Israel will finish it. Hamas will understand that by attacking us, they have made a mistake of historic proportions.  We will exact a price that will be remembered by them and Israel's other enemies for decades to come. The savage attacks that Hamas perpetrated against innocent Israelis are mindboggling: slaughtering families in their homes, massacring hundreds of young people at an outdoor festival, and kidnapping scores of women, children and elderly, even Holocaust survivors. Hamas terrorists bound, burned and executed children. They are savages. Hamas is ISIS. And just as the forces of civilization united to defeat ISIS, the forces of civilization must support Israel in defeating Hamas. In fighting Hamas, Israel is not only fighting for its own people. It is fighting for every country that stands against barbarism. Israel will win this war, and when Israel wins, the entire civilized world will win."

# Tokenization and sentence splitting
sentences = sent_tokenize(speech)
words = [word_tokenize(sentence) for sentence in sentences]

# Stopwords removal
stop_words = set(stopwords.words('english'))
filtered_words = [[word.lower() for word in words if word.isalnum() and word.lower() not in stop_words] for words in words]

# Calculate word frequencies
fdist = FreqDist(word for sentence in filtered_words for word in sentence)

# Extract keywords (most frequent words)
keywords = fdist.most_common(10)

# Sentiment analysis
analyzer = SentimentIntensityAnalyzer()
sentiments = [analyzer.polarity_scores(sentence) for sentence in sentences]

# Output results
print("Sentences:")
for i, sentence in enumerate(sentences):
    print(f"{i+1}: {sentence}")

print("\nKeywords:")
for word, frequency in keywords:
    print(f"{word}: {frequency}")

print("\nSentiment Analysis:")
for i, sentiment in enumerate(sentiments):
    print(f"Sentiment of Sentence {i+1}: {sentiment}")

# Reconstruct filtered text
#filtered_text = [TreebankWordDetokenizer(sentence) for sentence in filtered_words]
#filtered_speech = ' '.join(filtered_text)

#print("\nFiltered Speech:")
#print(filtered_speech)
