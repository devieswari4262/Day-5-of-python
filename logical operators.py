#logical operators
#find the give number is leap year or not
year=int(input("enter the year:"))

if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not a leap year")
o/p:enter the year:1994
not a leap year
enter the year:2024
leap year


number=int(input("enter the number:"))
if(number%5==0):
    print("divisible by 5")
else:
    print("not divisible by 5")
o/p:enter the number:65
divisible by 5

#find out the largest number between the three numbers

first_number=int(input("enter the first number:"))
second_number=int(input("enter the second_number:"))
third_number=int(input("enter the third number:"))
if (first_number>second_number and first_number>third_number ):
    print("first is the largest number")
elif(second_number>first_number and second_number>third_number):
    print("second number is the largest number")
else:
    print("third number is the largest number")
o/p:enter the first number:8
enter the second_number:7
enter the third number:9
third number is the largest number

