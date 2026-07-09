s = "aabbccddef"

feq=dict()

for i in range(len(s)):
    if s[i] in feq:
        feq[s[i]] += 1
    else:
        feq[s[i]] = 1

for k,v in feq.items():
    if v == 1:
        print(k)
        break
