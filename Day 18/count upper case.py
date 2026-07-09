s = "PyTHonAI"
count= 0
for i in range(len(s)):
    if s[i].isupper():
        count += 1
        
print("Total uppercase letters found:",count)
