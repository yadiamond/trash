import math
n, k = map(int, input().split(' '))
al = list(map(int, input().split(' ')))
q = int(input())
ql = []
for i in range(q):
    l, r = (map(int, input().split(' ')))
    l -= 1
    ql.append([l, r])
for i in range(len(al)):
    x = 0
    for j in range(len(ql)):
        if i >= ql[j][0] and i < ql[j][1]:
            x += 1
    if x != 0:
        al[i] = math.ceil(al[i] // x)
    else:
        al[i] = 0

i = 0
while i < len(al):
    if al[i] == 0:
        al.remove(al[i])
    i += 1

while k > 1:
    al.pop(al.index(min(al)))
    k -= 1
if al == []:
    print(-1)
else:
    print(min(al))