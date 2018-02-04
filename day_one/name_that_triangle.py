# Read
s1 = float(input("Enter the side of side 1: "))
s2 = float(input("Enter the length of side 2: "))
s3 = float(input("Enter the length of side 3: "))

#Determine
if s1 == s2 and s2 == s3:
	name = "equilateral"
elif s1 == s2 or s2 == s3 or s3 == s1:
	name = "isocesles"
else:
	name = "scalene"

#Display 
print("That's a", name, "triangle")