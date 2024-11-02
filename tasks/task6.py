n = int(input())
def harshad(n):
    l = []
    x = 1
    while len(l) < n:
        y = sum(map(int, list(str(x))))
        if x % y == 0:
            l.append(x)
        x += 1
    return l[(n - 1)]
print(harshad(n))