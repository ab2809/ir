# Data
docs = {
    "Anthony and Cleopatra": "Anthony is there, Brutus is Caeser is with Cleopatra mercy worser.",
    "Julius Ceaser": "Anthony is there, Brutus is Caeser is but Calpurnia is.",
    "The Tempest": "mercy worser",
    "Hamlet": "Caeser and Brutus are present with mercy and worser",
    "Othello": "Caeser is present with mercy and worser",
    "Macbeth": "Anthony is there, Caeser, mercy."
}

terms = ["Anthony", "Brutus", "Caeser", "Calpurnia", "Cleopatra", "mercy", "worser"]

# Create Vector Matrix
matrix = [[0 for _ in range(len(docs))] for _ in range(len(terms))]

texts = list(docs.values())

for i in range(len(terms)):
    for j in range(len(texts)):
        if terms[i].lower() in texts[j].lower():
            matrix[i][j] = 1

print("Vector Matrix")
for i in range(len(terms)):
    print(terms[i], ":", matrix[i])

# Convert to Bit Pattern
bits = {}

for i in range(len(terms)):
    bit = ""

    for x in matrix[i]:
        bit += str(x)

    bits[terms[i]] = int(bit, 2)

print("\nBit Values")
for k, v in bits.items():
    print(k, ":", bin(v))


# Search Query
def search(query):

    q = query

    # Replace words with bit values
    for term in terms:
        if term in q:
            q = q.replace(term, str(bits[term]))

    # Replace logical operators
    q = q.replace("AND", "&").replace("and", "&")
    q = q.replace("OR", "|").replace("or", "|")
    q = q.replace("NOT", "~").replace("not", "~")

    print("\nConverted Query :", q)

    result = eval(q)

    result_bin = bin(result)[2:].zfill(len(docs))

    print("Result :", result_bin)

    print("Matching Plays")

    names = list(docs.keys())

    for i in range(len(result_bin)):
        if result_bin[i] == "1":
            print("-", names[i])


# User Input
while True:

    query = input("\nEnter Query (EXIT to stop): ")

    if query.lower() == "exit":
        break

    search(query)