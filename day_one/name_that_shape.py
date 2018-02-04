#Read 
nsides = int(input("Enter the number of sides: "))

#Determine the name
name = ""
if nsides == 3:
	name = "triangle"
elif nsides == 4:
	name = "quadrilateral"
elif nsides == 5:
	name = "pentagon"


#Display an error message or the name of the polygon
if name == "":
	print("That number of sides is not supported by this program.")
else:
	print("That's a", name)