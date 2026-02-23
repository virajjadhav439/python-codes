# Discount Giver
Amount=int(input("Enter Your Purchase Amount : "))
if Amount<499:
    print("No Discount!!!")
    print("Your Total Bill is : ",Amount)
elif 499<Amount and Amount<=2000:
    print("10% Discount!!!")
    print("Your Total Bill is : ",Amount*(1-0.1))
elif 2000<Amount and Amount<5000:
    print("15% Discount!!!")
    print("Your Total Bill is : ",Amount*(1-0.15))
else:
    print("25% Discount!!!")
    print("Your Total Bill is : ",Amount*(1-0.25))

