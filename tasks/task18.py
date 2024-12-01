import math
n = int(input())
if n <= 6:
    print(1)
else:
    print(1 + math.ceil((n - 6) / 4))
    print(max(1 ,1 + (n - 3) // 4))
