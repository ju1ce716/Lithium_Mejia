def sum_of_sqr(n):
total = 0
    for i in range(1, n + 1):
        total += i**2
    return total

n = 0
while n < 1 or n > 100:
    n = input("Enter a Number from 1 to 100 : ")
    n = int(n)

print("Sum of all squared numbers is" sum_of_sqr(n))
