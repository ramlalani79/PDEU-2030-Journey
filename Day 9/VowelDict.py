word = "banana"

feq= dict()

for i in range(len(word)):
    if word[i] in feq:
        feq[word[i]] += 1
    else:
        feq[word[i]] = 1

print(feq)
