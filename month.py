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
else:
    print("error")
