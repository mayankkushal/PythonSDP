data=[]
num=int(input("enter a number(0 to quit):"))
while num!=0 :
    data.append(num)
    num=int(input("enter a number:"))
data.sort()
print(data)
