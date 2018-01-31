#!/usr/bin/python

import re
import string
import numpy as np
import matplotlib.pyplot as plt

#creating initial dictionary and stopword list
frequency = {}
flimit = 7
#stopword list from Alir3z4/stop-words
stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]

#open document, save to variable as lowercase words
document_text = open('speech.txt', 'r')
text_string = document_text.read().lower()

#split the string into words and sort out the stopwords
querywords = text_string.split()
resultwords = [word for word in querywords if word not in stopwords]
text_string = ' '.join(resultwords)

#regular expression
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

#loop through the words and count the unique word, saving to dictionary
for word in match_pattern:
	count = frequency.get(word,0)
	frequency[word] = count + 1

#sort the dictionary by values, save to list of tuples, only words said 7+ times
frequency = sorted(frequency.items(), key=lambda x:x[1])
frequency = [i for i in frequency if i[1] >= flimit]

#split list of tuples into two lists
bars,height = map(list,zip(*frequency))

#set the bars and labels into matplot
y_pos = np.arange(len(bars))
plt.barh(y_pos, height)
plt.yticks(y_pos, bars)

#generate graph
plt.show()
