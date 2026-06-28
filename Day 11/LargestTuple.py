t = (10,80,20,50,100)
n = t[0]
largest = n 
for i in t:
    if i > largest:
        largest = i

print("The largest number in the tuple is:", largest)
