n = int(input("Enter the number of stars: "))

for i in range(0, n):
    for j in range(0, i+1):

        # printing stars
        print("* ",end="")

    # ending line after each row
    print("\r")
