def greet_students(name, nChar):
    #Limit iterations to the actual length of the string
    limit = min(nChar, len(name))
    for i in range(limit):
        print(name[i])

name = input("Enter a Name : ")
nChar = input("Enter any numeric number : ")
nChar = int(nChar)
greet_students(name, nChar)
