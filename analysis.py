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
