s = "I Love Python"

print(s.replace(" ",""))

# 2 method

s = "I Love Python"

n = ""

for i in s:
    if i != " ": # != does not equal to
        n += i

print(n)
