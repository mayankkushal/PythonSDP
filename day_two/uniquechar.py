s=input("enter a string")
char={}
for ch in s:
    char[ch]=True
print("there are",len(char),"unique characters")
