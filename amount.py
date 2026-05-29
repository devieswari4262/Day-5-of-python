#condition statement
#caluclate the purchase amount, apply the discount and print the final payable amount

amount = int(input("Enter the amount:"))
if amount < 1000:
    discount = 0.05
elif 1000 <= amount < 5000:
    discount = 0.10
else:
    discount = 0.15
final_amount = amount - (amount * discount)
print(f"Final amount is {final_amount}")
print("Final amount after two decimal points:", round(final_amount, 2))
