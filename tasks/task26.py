#task: https://leetcode.com/problems/pascals-triangle-ii/description/
class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            ans = [[1], [1, 1]]
            for i in range(2, rowIndex + 1):
                ansx = [1]
                for j in range(len(ans[i - 1]) // 2):
                    ansx += [ans[i - 1][j] + ans[i - 1][j + 1]]
                if len(ans[i - 1]) % 2 == 0:
                    ansx += reversed(ansx[:-1])
                else:
                    ansx += reversed(ansx)
                ans += [ansx]
        return ans[-1]