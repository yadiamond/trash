#task: https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, rowIndex):
        if rowIndex == 1:
            return [1]
        elif rowIndex == 2:
            return [1, 1]
        else:
            ans = [[1], [1, 1]]
            for i in range(2, rowIndex):
                ansx = [1]
                for j in range(len(ans[i - 1]) // 2):
                    ansx += [ans[i - 1][j] + ans[i - 1][j + 1]]
                if len(ansx) % 2 == 0:
                    ansx += reversed(ansx)
                else:
                    ansx += reversed(ansx[:-1])
                return ansx