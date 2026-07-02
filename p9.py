# 1) Implement Inverted Index
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
stop_words = stopwords.words("english")

index = {}
freq1 = {}
freq2 = {}

doc1 = "The quick brown fox jumped over the lazy dog"
doc2 = "The lazy dog slept in the sun"

tokens1 = doc1.lower().split()
tokens2 = doc2.lower().split()

terms = list(set(tokens1 + tokens2))

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

for term, docs in index.items():
    print(term, "->", end=" ")

    for doc in docs:
        freq = freq1 if doc == "Document1" else freq2
        print(f"{doc} ({freq.get(term,0)})", end=" ")

    print()

#2
for term in sorted(index):
    print(term, "->", end=" ")

    for doc in index[term]:
        freq = freq1 if doc == "Document1" else freq2
        print(f"{doc} ({freq.get(term,0)})", end=" ")

    print()

#3 unique terms
print("\nTotal Unique Terms :", len(index))
