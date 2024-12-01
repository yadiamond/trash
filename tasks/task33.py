x = int(input())
y = int(input())
k = int(input())
ans = 0
kx = x // k
ky = y // k
ans += kx + ky
if x - kx * k > (kx + 1) * k - x:
    ans += (kx + 1) * k - x + 1
else:
    ans += x - kx * k
if y - ky * k > (ky + 1) * k - y:
    ans += (ky + 1) * k - y + 1
else:
    ans += y - ky * k
print(ans)