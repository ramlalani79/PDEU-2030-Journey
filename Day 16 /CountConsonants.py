s = "python"

count = 0
for i in range(len(s)):
    if s[i] in "bcdfghjklmnpqrstvwxyz":
        count +=1

print("Number of consonants in the string:", count)
