n = int(input("Enter a Number:"))

if n % 2 == 0 and (n < 6 or n > 20):
    print("Not Weird")
else:
	print ("Weird")