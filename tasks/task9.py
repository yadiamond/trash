import math

def f1(n, m):
    x = math.ceil(n / 2)
    y = math.ceil(n / 2)
    ans = 0
    ans += (n - 1) + (m - 1) + (min((math.floor((n - 1) / 2)), (math.floor((m - 1) / 2)))) + (min((math.floor((n - 1) / 2), (math.ceil((m - 1) / 2))))) + min((math.ceil((n - 1) / 2)), (math.floor((m - 1) / 2))) + min(math.ceil((m - 1) / 2), math.ceil((n - 1) / 2))
    return ans
