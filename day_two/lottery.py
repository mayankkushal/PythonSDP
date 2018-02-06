from random import randrange
min=1
max=49
length=6
ticket_num=[]
for i in range(length):
    r= randrange(min,max+1)
    while r in ticket_num:
        r= randrange(min,max+1)
    ticket_num.append(r)

ticket_num.sort()
print("ticket numbers are:")
for i in ticket_num:
    print(i)
