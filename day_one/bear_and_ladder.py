t = int(input())
for i in range(t):
    x,y = input().split()
    x,y = int(x), int(y)
    if x < y:
        x,y = y,x
    if x-y == 2:
        print("YES")
        continue
    if x-y == 1 and x % 2 == 0:
        print("YES")
        continue
    print("NO")

'''
Input:

7
1 4
4 3
5 4
10 12
1 3
999999999 1000000000
17 2384823

Output:
NO
YES
NO
YES
YES
YES
NO
'''