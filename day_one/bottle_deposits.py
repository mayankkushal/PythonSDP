LESS_DEPOSIT = 0.10
MORE_DEPOSITE = 0.25

#Read inputfrom the user
less = int(input("How many containers 1 litre or less do you have? "))
more = int(input("How many containers more than 1 litre do you have? "))

#Compute the refund amount
refund = less * LESS_DEPOSIT + more * MORE_DEPOSITE

#Display the result
print("Your total refund will be $%.2f."% refund)