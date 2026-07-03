# 6. Compute Similarity between Two Text Documents

import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))  # Initialize


file1 = open("text1.txt").read().lower()
file2 = open("text2.txt").read().lower()      # Read Files

# Tokenize
words1 = word_tokenize(file1)
words2 = word_tokenize(file2)

tokens1 = []
tokens2 = []

freq1 = {}
freq2 = {}

v1 = []
v2 = []



# Remove Stopwords
for word in words1:
    if word.isalpha() and word not in stop_words:
        tokens1.append(word)

for word in words2:
    if word.isalpha() and word not in stop_words:
        tokens2.append(word)

# Count Frequency
for word in tokens1:
    if word in freq1:
        freq1[word] += 1
    else:
        freq1[word] = 1

for word in tokens2:
    if word in freq2:
        freq2[word] += 1
    else:
        freq2[word] = 1

# Unique Words
all_words = list(set(tokens1 + tokens2))

# Create Vectors
for word in all_words:

    if word in freq1:
        v1.append(freq1[word])
    else:
        v1.append(0)

    if word in freq2:
        v2.append(freq2[word])
    else:
        v2.append(0)

# Cosine Similarity
dot = np.dot(v1, v2)
mag1 = np.linalg.norm(v1)
mag2 = np.linalg.norm(v2)

similarity = dot / (mag1 * mag2)

print("Cosine Similarity:", similarity)
