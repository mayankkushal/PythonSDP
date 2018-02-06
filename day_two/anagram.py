def charcount(s):
    count={}
    for ch in s:
        if ch in count:
            count[ch]=count[ch]+1
        else:
            count[ch]=1
    return count

def main():
    s1=input("first string:")
    s2=input("second string:")
    counts1=charcount(s1)
    counts2=charcount(s2)
    if counts1==counts2:
        print("anagram")
    else:
        print("not anagram")
main()
