SQFT_PER_ACRE = 435.60

#Read input from user
length = float(input("Enter the length of the room in feet "))
breadth = float(input("Enter the breadth of the room in feet "))

#Compute theare in acres
acres = length * breadth / SQFT_PER_ACRE

#Display the result
print("The area of the field is", acres, "acres")