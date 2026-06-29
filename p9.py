# PRACTICAL 9 – Inverted Index
# Learn Program 1 properly.
# Then Program 3 is just Program 1 + sorted().
# Program 4 is Program 3 + len(inverted_index).

#1) Implement Inverted Index Concept

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')
# Documents
doc1 = "The quick brown fox jumped over the lazy dog"
doc2 = "The lazy dog slept in the sun"
# Tokenization
tokens1 = doc1.lower().split()
tokens2 = doc2.lower().split()
# Unique Terms
terms = list(set(tokens1 + tokens2))
# Inverted Index
index = {}
freq1 = {}
freq2 = {}
for term in terms:
    if term in stop_words:
        continue
    docs = []
    if term in tokens1:
        docs.append("Document1")
        freq1[term] = tokens1.count(term)
    if term in tokens2:
        docs.append("Document2")
        freq2[term] = tokens2.count(term)
    index[term] = docs
# Display Inverted Index
for term, docs in index.items():
    print(term, "->", end=" ")
    for doc in docs:
        freq = freq1 if doc == "Document1" else freq2
        print(f"{doc} ({freq.get(term,0)})", end=" ")
    print()

#3) Display Inverted Index in Alphabetical Order

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = stopwords.words('english')

# Documents
doc1 = "The quick brown fox jumped over the lazy dog"
doc2 = "The lazy dog slept in the sun"

# Tokenization
tokens1 = doc1.lower().split()
tokens2 = doc2.lower().split()

# Unique Terms
terms = list(set(tokens1 + tokens2))

# Inverted Index
index = {}
freq1 = {}
freq2 = {}

for term in terms:

    if term in stop_words:
        continue

    docs = []

    if term in tokens1:
        docs.append("Document1")
        freq1[term] = tokens1.count(term)

    if term in tokens2:
        docs.append("Document2")
        freq2[term] = tokens2.count(term)

    index[term] = docs

# Display Alphabetically
for term in sorted(index.keys()):

    print(term, "->", end=" ")

    for doc in index[term]:
        freq = freq1 if doc == "Document1" else freq2
        print(f"{doc} ({freq.get(term,0)})", end=" ")

    print()

✅ 4) Count Total Unique Terms
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')
# Documents
doc1 = "The quick brown fox jumped over the lazy dog"
doc2 = "The lazy dog slept in the sun"
# Tokenization
tokens1 = doc1.lower().split()
tokens2 = doc2.lower().split()
# Unique Terms
terms = list(set(tokens1 + tokens2))
# Inverted Index
index = {}
freq1 = {}
freq2 = {}
for term in terms:
    if term in stop_words:
        continue
    docs = []
    if term in tokens1:
        docs.append("Document1")
        freq1[term] = tokens1.count(term)
    if term in tokens2:
        docs.append("Document2")
        freq2[term] = tokens2.count(term)
    index[term] = docs
print("Inverted Index (Alphabetical Order)\n")
for term in sorted(index.keys()):
    print(term, "->", end=" ")
    for doc in index[term]:
        freq = freq1 if doc == "Document1" else freq2
        print(f"{doc} ({freq.get(term,0)})", end=" ")
    print()
total_terms = len(index)
print("\nTotal Unique Terms :", total_terms)

✅ 2) Retrieve Document based on Query
import string
from collections import defaultdict

# Preprocess Text
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

# Build Inverted Index
def build_index(docs):

    index = defaultdict(set)

    for doc, text in docs.items():

        words = preprocess(text)

        for word in words:
            index[word].add(doc)

    return index

# Search Query
def search(index, query):

    terms = preprocess(query)

    result = None

    for term in terms:

        if term in index:

            if result is None:
                result = index[term]

            else:
                result = result.intersection(index[term])

        else:
            return set()

    return result if result else set()

# Documents
docs = {
    1: "Information retrieval is an essential aspect of search engines.",
    2: "The field of information retrieval focuses on algorithms.",
    3: "Search engines use retrieval techniques to improve performance.",
    4: "Deep learning models are used for information retrieval tasks."
}

# Build Index
index = build_index(docs)

# Search
query = "retrieval"

result = search(index, query)

print("Documents containing", query, ":", sorted(result))