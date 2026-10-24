sentence = "the cat and the hat and the bat"
words = sentence.split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)
most_common = max(counts, key=counts.get)
print(most_common, counts[most_common])