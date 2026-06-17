num = [10,20,30,40,50,60,70]
target = 50

def binarysearch(num, target):
    n = len(num)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if num[mid] == target:
            return mid

        elif num[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1

result = binarysearch(num, target)
print(result)