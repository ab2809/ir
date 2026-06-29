# Input
text1 = input("Enter Text 1: ").lower().split()
text2 = input("Enter Text 2: ").lower().split()

# BIGRAM
bigram1 = []
bigram2 = []

for i in range(len(text1)-1):
    bigram1.append((text1[i], text1[i+1]))

for i in range(len(text2)-1):
    bigram2.append((text2[i], text2[i+1]))

print("\nBigrams of Text 1:")
for bg in bigram1:
    print(bg)

print("\nBigrams of Text 2:")
for bg in bigram2:
    print(bg)

# TRIGRAM 
trigram1 = []
trigram2 = []

for i in range(len(text1)-2):
    trigram1.append((text1[i], text1[i+1], text1[i+2]))

for i in range(len(text2)-2):
    trigram2.append((text2[i], text2[i+1], text2[i+2]))

print("\nTrigrams of Text 1:")
for tg in trigram1:
    print(tg)

print("\nTrigrams of Text 2:")
for tg in trigram2:
    print(tg)

# BIGRAM JACCARD 
set1 = set(bigram1)
set2 = set(bigram2)

bigram_jaccard = len(set1 & set2) / len(set1 | set2)

print("\nBigram Jaccard Coefficient:", bigram_jaccard)

# TRIGRAM JACCARD 
set1 = set(trigram1)
set2 = set(trigram2)

if len(set1 | set2) == 0:
    trigram_jaccard = 0
else:
    trigram_jaccard = len(set1 & set2) / len(set1 | set2)

print("Trigram Jaccard Coefficient:", trigram_jaccard)