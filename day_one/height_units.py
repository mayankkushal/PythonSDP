'''
Convert a height in feet and inches to centimeters
'''

IN_PER_FT = 12
CM_PER_IN = 2.54

#Read input from user
print("Enter your height: ")
feet = int(input("Number of feet: "))
inches = int(input("Number of inches: "))

#Compute the equivalent number of centimeters
cm = (feet * IN_PER_FT + inches) * CM_PER_IN

#Display the result
print("Your height in centimeters is: ", cm)