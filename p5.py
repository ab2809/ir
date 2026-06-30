# PageRank Algorithm
d = 0.85
links = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"]
}
out = {
    "A": 2,
    "B": 1,
    "C": 1
}
pr = {
    "A": 1,
    "B": 1,
    "C": 1
}
print("Iteration 0")
print(pr)

for i in range(1, 3):
    new = {}
    for page in links:
        total = 0
        for link in links:
            if page in links[link]:
                total += pr[link] / out[link]
        new[page] = (1-d) + d * total
    pr = new
    print("\nIteration", i)
    print(pr)
