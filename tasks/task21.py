#task: https://leetcode.com/problems/defuse-the-bomb/?envType=daily-question&envId=2024-11-18
class Solution:
    def decrypt(self, code, k):
        x = len(code)
        for i in range(len(code)):
            sum = code[(i + 1 - x)] + code[(i + 2 - x) + code[(i + 3 - x)]]
            code = code[:i] + [sum] + code[i + 1:]
            
