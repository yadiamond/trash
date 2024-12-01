n = int(input())
def func1(n):
    x = n
    ans = []
    for i in range(9, 1, -1):
        while n % i == 0:
            n = n / i
            ans += [str(i)]
    if n == 1:
        if ans == []:
            print(1)
        else:
            print(int(''.join(reversed(ans))))
    else:
        print(-1)
def func2(n):
    ans = ""
    for d in range( 9 , 1 , -1):
        while n % d == 0 :
            n //= d
            ans = str ( d ) + ans
    if n == 1 :
        print( ans or "1" )
    else:
        print(-1)
func1(n)
func2(n)