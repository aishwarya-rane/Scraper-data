#libraries
import nltk
from nltk.corpus
import random

# Load and prepare the dataset
documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# Define the feature extractor
all_words = nltk.FreqDist(w.lower() for word in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

# Train Naive Bayes classifier
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)


# Show the most important features as interpreted by Naive Bayes
classifier.show_most_informative_features(5)

"""
Most Informative Features
       contains(winslet) = True              pos : neg    =       : 1.0
     contains(illogical) = True              neg : pos    =       : 1.0
      contains(captures) = True              pos : neg    =       : 1.0
        contains(turkey) = True              neg : pos    =       : 1.0
        contains(doubts) = True              pos : neg    =       : 1.0
"""
