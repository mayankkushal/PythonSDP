words=[]
while True:
    word=input("enter a word(blank to exit):")
    if word=="":
        break
    if word not in words:
        words.append(word)
for word in words:
    print(word)
