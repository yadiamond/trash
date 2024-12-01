a = int(input())
b = int(input())
c = int(input())
maximum = max(a, b, c)
minimum = min(a, b, c)
mid = a + b + c - maximum - minimum
if maximum - mid == mid - minimum and maximum * minimum == mid ** 2:
    print('B', minimum, mid, maximum)
elif maximum - mid == mid - minimum and maximum - mid > 0:
    print('A', minimum, mid, maximum)
elif maximum * minimum == mid ** 2:
    print('G', minimum, mid, maximum)
else:
    print('No')