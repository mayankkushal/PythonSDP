def reverse(data,value):
    keys=[]
    for key in data:
        if data[key]==value:
            keys.append(key)
    return keys
def main():
    d={"a":1,"b":2,"c":3,"e":2}
    print(reverse(d,2))
main()
