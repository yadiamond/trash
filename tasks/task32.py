#task: https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, columnTitle):
        s = list(columnTitle).reverse()
        ans = 0
        for i in range(len(s)):
            ans += (ord('A') - ord(s[i]) + 1) * 26 ** i
        return ans 
        