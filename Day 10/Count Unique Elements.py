nums = [1, 2, 2, 3, 4, 4, 5]

n=[]

for i in nums:
    if i not in n:
        n.append(i)

print("count of unique numbers:" , len(n))
