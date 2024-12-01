z = list(map(int, input().split()))
for i in range(z[0]):
    c = list(map(int, input().split()))
    if c[1] / c[0] > z[1] / 100:
        continue
    else:
        print('bad')
        break
else:
    print('good')
    