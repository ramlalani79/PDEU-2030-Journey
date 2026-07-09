s = input("Enter a sentence: ")

words = s.split()

for i in words:
    rev = ""
    for j in i :
        rev = j + rev
    print(rev)
