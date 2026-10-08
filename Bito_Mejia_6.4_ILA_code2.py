def greet_students(name, nChar):
    #Fixed syntax error with ':' and updated slice to create an inverted triangle
    for i in range(nChar):
        print(name[0 : nChar - i])

name = input("Enter a Name: ")
greet_students(name, len(name))
