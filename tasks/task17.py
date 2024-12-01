#task: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/?envType=daily-question&envId=2024-11-14
import math
class Solution:
    def minimizedMaximum(self, n, quantities):
        quantities.sort()
        while quantities[0] < k:
            n -= 1
            quantities.pop(0)
            k = math.ceil(sum(quantities) / n)
        return math.ceil(sum(quantities) / n)
        