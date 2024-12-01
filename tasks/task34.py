import math
s = input()
ans = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        ans += 1
        s = s[:i] + f'{int(math.fabs(int(s[i]) - 1))}' + s[i + 1:]
print(ans)