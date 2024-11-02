x = list(map(float, input().split()))
GA = x[0]
AB = x[1]
R1 = x[2]
R2 = x[3]
ans = (R2 + (GA + AB) * (R1-R2) / AB)
print(f'{ans:.3f}')