import string

amt_of_words = {}

with open("poem.txt", "r") as f:
    for line in f:
        words = (
            line.translate(str.maketrans("", "", string.punctuation))
            .replace("\n", " ")
            .split(" ")
        )
        for word in words:
            if word not in amt_of_words:
                amt_of_words[str(word)] = 1
            else:
                amt_of_words[str(word)] += 1

print(amt_of_words)
