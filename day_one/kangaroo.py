x1, v1, x2, v2 = input("Enter x1 v1 x2 v2 in the same order:").strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

# Since x1<x2 (given in the question)
if v1 <= v2:
	print("NO")

if (x1 - x2) % (v1 - v2) == 0:
	print('YES')

else:
	print("NO")
