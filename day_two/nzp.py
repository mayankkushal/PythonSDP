n=[]
z=[]
p=[]
while True:
    line=input("enter an int(blank to exit):")
    if line=="":
        break
    num=int(line)
    if num<0:
        n.append(num)
    elif num>0:
        p.append(num)
    else:
        z.append(num)
for i in n:
    print(i)
for i in n:
    print(i)
for i in z:
    print(i)
