import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
quadgram_measures = nltk.collocations.QuadgramAssocMeasures()

with open('results.txt') as wordfile:
    text = wordfile.read()

tokens = nltk.wordpunct_tokenize(text)

# change this to read in your data
finder = BigramCollocationFinder.from_words(tokens)

# only bigrams that appear n+ times
finder.apply_freq_filter(2)
# return the Z# n-grams with the highest pointwise mutual information (PMI)
#print(finder.nbest(bigram_measures.pmi, 10))
print(finder.nbest(trigram_measures.pmi, 10))
#print(finder.nbest(quadgram_measures.pmi, 10))