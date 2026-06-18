def sum_recursion(n):
    if n == 0:
        return 0
    return n + sum_recursion(n - 1)

num = int(input("Enter a number: "))
print("Sum =", sum_recursion(num))
