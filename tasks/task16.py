#task: https://leetcode.com/problems/most-beautiful-item-for-each-query/description/?envType=daily-question&envId=2024-11-12
class Solution:
    def maximumBeauty(self, items, queries):
        ans = []
        sorted_items = sorted(items, key = lambda x: x[1], reverse = True)
        for i in queries:
            for j in sorted_items:
                if j[0] <= i:
                    ans += [j[1]]
                    break
            else:
                ans += [0]
        return ans
    