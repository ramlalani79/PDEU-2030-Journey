arr = [10,50,20,90,40]
n=arr[0]
for i in arr:
    if i>n:
        n=i
print(n)


or


arr = [10,50,20,90,40]
arr.sort()
print(arr[-1])
