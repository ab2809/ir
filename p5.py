# PageRank for 3 pages: A, B, C
# Using formula: PR(A) = (1-d) + d * Σ ( PR(Bi) / C(Bi) )

# PageRank Algorithm

d = 0.85
links = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A']
}
pages = list(links.keys())
out = {p: len(links[p]) for p in pages}
pr = {p: 1.0 for p in pages}

print("Iteration 0")
for p in pages:
    print(f"PR({p}) = {pr[p]:.6f}")
for i in range(1, 3):
    new_pr = {}
    for p in pages:
        total = 0
        for q in pages:
            if p in links[q]:
                total += pr[q] / out[q]
        new_pr[p] = (1-d) + d * total
    pr = new_pr
    print(f"\nIteration {i}")
    for p in pages:
        print(f"PR({p}) = {pr[p]:.6f}")