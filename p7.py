#a. Direct text

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

text = input("Enter Text: ")
stop_words = set(stopwords.words('english'))
words = word_tokenize(text)

filtered = []
for word in words:
    if word.lower() not in stop_words:
        filtered.append(word)
print("Original Words :", words)
print("After Stopword Removal :", filtered)

# b. reading text from a text file & importing it in a text file
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
read_file = open("input.txt", "r")
write_file = open("output.txt", "w")
words = read_file.read().split()
filtered = []
for word in words:
    if word.lower() not in stop_words:
        filtered.append(word)
        write_file.write(word + " ")
print("After Stopword Removal :", filtered)
read_file.close()
write_file.close()