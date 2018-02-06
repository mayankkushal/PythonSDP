string = input("Enter string:")
count1 = 0
count2 = 0
count3 = 0
for i in string:
    if(i.islower()):
        count1 += 1
    elif(i.isupper()):
        count2 += 1
    elif(i.isdigit()):
        pass
    else:
        count3 += 1

print("The number of lowercase characters is: ")
print(count1)
print("The number of uppercase characters is: ")
print(count2)
print("The number of special characters is: ")
print(count3)
