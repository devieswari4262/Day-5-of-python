#condition statement
#Calculate the total parking fee based on number of hours
# Test cases:
# test case1:
# input:2
# output:200
#  test case2:
#input:6
#output:370
#  test case2:
#input:six
#output:error


try:
    hours=int(input("Enter the number of hours:"))
except:
    print("error")
if hours<=2:
    fee=hours*100
elif hours<5:
    fee(2*100)+(hours-2)*50
else:
    fee=(2*100)+(3*50)+(hours-5)*20
    print(fee)