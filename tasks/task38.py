#task: https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n):
        b = bin(n)[2:]
        ans = (str(b)).count('1')
        return ans