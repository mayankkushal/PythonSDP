#Read
grade = input("Enter grade: ")

#Compute
if grade == "S" or grade == "s":
	point = 10
elif grade == "A" or grade == "a":
	point = 9
elif grade == "B" or grade == "b":
	point = 8
elif grade == "C" or grade == "c":
	point = 7
elif grade == "D" or grade == "d":
	point = 6
elif grade == "E" or grade == "e":
	point = 5
else:
	point = 0

#Display
print("Your grade", grade,"corressponds to", point,"points")