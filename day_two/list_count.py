def countrange(data,min,max):
    count=0
    for e in data:
        if min<=e and e<max:
            count=count+1
    return count
def main():
    data=[1,2,3,4,5,6,7,8]
    print(countrange(data,2,6))
main()
