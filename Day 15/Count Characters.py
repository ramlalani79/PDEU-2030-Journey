s = "banana"

feq=dict()

for i in range(len(s)):
    if s[i] in feq:
        feq[s[i]] += 1
    else:
         feq[s[i]] = 1

for key, value in feq.items():
    print(key,"=",value)
