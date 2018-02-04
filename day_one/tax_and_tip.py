'''
Compute tax and tip for a restraunt meal
'''
TAX_RATE = 0.05
TIP_RATE = 0.18

#Read cost of meal from the user
cost = float(input("Enter the cost of the meal: "))

#Compute the tax and the tip
tax = cost * TAX_RATE
tip = cost * TIP_RATE
total = cost + tax + tip

#Display the result
print("THe tax is %.2f and the tip is %.2f, making the total %.2f" % (tax, tip, total))