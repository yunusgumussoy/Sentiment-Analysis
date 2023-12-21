# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 18:15:57 2023

@author: Yunus
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Benjamin Netanyahu's speech, Oct 10th, 2023
speech = "Israel is at war. We didn't want this war. It was forced upon us in the most brutal and savage way. But though Israel didn't start this war, Israel will finish it. Hamas will understand that by attacking us, they have made a mistake of historic proportions.  We will exact a price that will be remembered by them and Israel's other enemies for decades to come. The savage attacks that Hamas perpetrated against innocent Israelis are mindboggling: slaughtering families in their homes, massacring hundreds of young people at an outdoor festival, and kidnapping scores of women, children and elderly, even Holocaust survivors. Hamas terrorists bound, burned and executed children. They are savages. Hamas is ISIS. And just as the forces of civilization united to defeat ISIS, the forces of civilization must support Israel in defeating Hamas. In fighting Hamas, Israel is not only fighting for its own people. It is fighting for every country that stands against barbarism. Israel will win this war, and when Israel wins, the entire civilized world will win."

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Tokenize the speech into sentences
sentences = nltk.sent_tokenize(speech)

# Perform sentiment analysis for each sentence
sentiment_scores = []
for sentence in sentences:
    sentiment = analyzer.polarity_scores(sentence)
    sentiment_scores.append(sentiment)

# Calculate overall sentiment scores
compound_scores = [sentiment['compound'] for sentiment in sentiment_scores]
average_compound = sum(compound_scores) / len(compound_scores)

# Determine the overall sentiment of the speech
overall_sentiment = "Positive" if average_compound > 0.05 else "Negative" if average_compound < -0.05 else "Neutral"

# Output results
print("Sentiment Analysis for Each Sentence:")
for i, sentiment in enumerate(sentiment_scores):
    print(f"Sentence {i+1} - Positive: {sentiment['pos']:.2f}, Negative: {sentiment['neg']:.2f}, Neutral: {sentiment['neu']:.2f}, Compound: {sentiment['compound']:.2f}")

print(f"\nOverall Sentiment of the Speech: {overall_sentiment} (Compound Score: {average_compound:.2f})")
