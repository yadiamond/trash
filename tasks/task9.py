l, r = map(int, input().split())
n = int(input())
l = [0]
for i in range(n):
    l += int(input()) + l[i]
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[j] - l[i] >= l and l[j] - l[i] <= r:
            print(l[i], l[j])
