data=[]
num=int(input("enter int:enter 0 to quit"))
while num!=0 :
    data.append(num)
    num=int(input("enter number:"))
data.reverse()
print(data)
