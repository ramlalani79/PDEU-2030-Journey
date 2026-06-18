num=int(input("plz enter a num = "))
fact=1
def show(num):
    if(num ==0 or num ==1):
        return 1
    else:
        fact = num * show(num - 1)
        return fact
print("the factorial of",num,"is",show(num))
