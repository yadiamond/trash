s = list(input())
s1 = list(sorted(s))
for i in range(len(s)):
    if s[i] == s1[i]:
        continue
    else:
        min_index = i + s[i:].index(min(s[i:]))
        
        s[i], s[min_index] = s[min_index], s[i]
        break
print(''.join(s))