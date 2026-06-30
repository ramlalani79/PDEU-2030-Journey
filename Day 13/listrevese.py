my_list=[5,4,3,2,1]
new_list=[]
for i in range(1, len(my_list) + 1):
    new_list.append(my_list[-i])
print(new_list)
