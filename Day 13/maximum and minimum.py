arr = [12,45,2,89,34]

maximum=arr[0]
minimum=arr[0]
for i in arr:
    if i > maximum :
        maximum = i
    
    elif i < minimum :
        minimum = i

 
print(maximum)   
print(minimum)
