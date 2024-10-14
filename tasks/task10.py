
def f1(n, m):
    P = n + m * 2
    p = P // 2
    ans = []
    for i in range(1, P):
        q = i * (p - i)
        if q.is_integer() and q > 0:
            ans.append(int(q))
    if ans:
        return max(ans)
    else:
        return 0


def f2(n1, n2):
    a = 2 * ( n2 // 4 )
    b = 2 * ( n2 // 4 )
    n2 %= 4
    if n2 >= 2 :
        n2 -= 2
        a += 2
    if n2 == 1 and n1 >= 2 :
        b += 2
        n2 = 0
        n1 -= 2
    while a < b and n1 >= 2 :
        a += 1
        n1 -= 2
    while a > b and n1 >= 2 :
        b += 1
        n1 -= 2
    a += n1 // 4
    b += n1 // 4
    n1 %= 4
    if n1 >= 2 :
        a += 1
    return (a * b)

for i in range(10):
    print(f1(), f2())