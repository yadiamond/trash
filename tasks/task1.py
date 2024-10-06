n = int (input())
m = int(input())
k = int(input())
c = int(input())
ans = m * (n // k)
n = n % k
ans += n * (m // k)
m = m % k
for i in range(1, n + 1):
    q = list(range(i, m + 1))
    ans += q.count(c)

print(ans)


n = int (input())
m = int(input())
k = int(input())
c = int(input())
ans = 0
ans += ( n // k ) * m
n %= k
ans += (m // k ) * n
m %= k
if c > m:
    n -= c - m
    c = m
if n > 0 :
    ans += min( c , n )
    c += k
    if c > m:
        n -= c - m
        c = m
        if n > 0 :
            ans += min( c , n )
print(ans)