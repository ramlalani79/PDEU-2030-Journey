arr = [1,0,2,3,0,4]

for i in range(len(arr)):
    if arr[i] == 0:
        arr.pop(i)
        arr.append(0)

print(arr)
