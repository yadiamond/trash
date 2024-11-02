a = int(input())
def func(a):
    x = 1
    while True:
        if (x * (a - 2 * x)) % 1 == 0:
            return x
            break
        else:
            x += 1
x = func(a)
print(x, (x * (a - 2 * x)))