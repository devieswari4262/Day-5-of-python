#condition statements
#A gym offeres membership plans based on the number of months enrolled.Write a code tocalculate the total membership cost.
Test cases:
Test case1
input:3
output:5000

Test case2
input:5
output:9000

Test case3
input:-1
output:invalid input

Month = int(input("Enter the month:"))
if Month < 0:
    print("invalid input")
elif Month == 1:   # colon was missing here
    print(0)
elif Month == 2 or Month == 3:
    print(5000)
elif Month >= 4 and Month <= 6:
    print(9000)
elif Month == 9:
    print(12000)
elif Month == 12:
    print(15000)

o/p: Enter the month:3
5000
Enter the month:5
9000
Enter the month:-1
invalid input
else:
    print("error")
