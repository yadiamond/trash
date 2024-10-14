n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l1 = []
for i in range(len(l)):
    q = l[i]
    if i == n - 1 and l[i-1] >= q:
        l1.append(l[i-1])
    elif q == 3 and i != 0:
        l1.append(l[i-1])
        l1.append(3 - l[i-1])
    elif q == 3 and i == 0:
        h = l[i + 1]
        l1.append(3 - h)
        l1.append(h)
    else:
        l1.append(q)
ans = 1
for i in range(1, len(l1)):
    if l1[i] != l1[i - 1]:
        ans += 1
print(ans)