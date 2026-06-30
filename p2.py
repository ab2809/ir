#1) Edit Distance between two strings
def edit(s1, s2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if s1[m-1] == s2[n-1]:
        return edit(s1, s2, m-1, n-1)

    return 1 + min(
        edit(s1, s2, m, n-1),
        edit(s1, s2, m-1, n),
        edit(s1, s2, m-1, n-1)
    )

str1 = input("Enter String 1: ")
str2 = input("Enter String 2: ")

print("Edit Distance is:", edit(str1, str2, len(str1), len(str2)))


#2) Weighted Edit Distance (Levenshtein Distance)
Code:
import numpy as np

def levenshtein(s1, s2):

    rows = len(s1) + 1
    cols = len(s2) + 1

    matrix = np.zeros((rows, cols))

    # First Column
    for i in range(rows):
        matrix[i][0] = i

    # First Row
    for j in range(cols):
        matrix[0][j] = j

    # Fill Matrix
    for i in range(1, rows):

        for j in range(1, cols):

            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(
                matrix[i-1][j] + 1,
                matrix[i][j-1] + 1,
                matrix[i-1][j-1] + cost
            )

    print("Matrix:\n", matrix)

    return int(matrix[rows-1][cols-1])


# Input
s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

print("Edit Distance :", levenshtein(s1, s2))

# 3) Word-Level Edit Distance (Sentence Level)
Code:
def edit_dist(w1, w2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if w1[m-1] == w2[n-1]:
        return edit_dist(w1, w2, m-1, n-1)

    return 1 + min(
        edit_dist(w1, w2, m, n-1),      # Insert
        edit_dist(w1, w2, m-1, n),      # Delete
        edit_dist(w1, w2, m-1, n-1)     # Replace
    )


# Input
s1 = input("Enter Sentence 1: ").split()
s2 = input("Enter Sentence 2: ").split()

print("Word Edit Distance :", edit_dist(s1, s2, len(s1), len(s2)))
