n = int(input())
ans = []
i = 2
while n >= 10:
    while n % i == 0:
        n //= i
        ans += [i]
    i += 1
ans += [n]

for i in range(len(ans) - 1, -1, -1):
    if ans[i] >= 10:
        print(-1)
        break
else:
    while ans[0] * ans[1] < 10:
        ans += ans[0] * ans[1]
        ans.pop(0)
        ans.pop(1)
        ans.sort()
    s = ''
    for i in ans:
        s += str(i)
    print(s)