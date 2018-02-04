n = int(input("Enter n: "))
lucky = 0
unlucky = 0
for i in range(0,n):
	weapons = int(input("Number of weapons that the ith soldier is holding: "))
	if weapons % 2 == 0:
		lucky += 1
	else: 
		unlucky += 1

if lucky > unlucky:
	print("Ready For Battle")
else:
	print("Not Ready")