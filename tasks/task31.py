#task: https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums):
        x = set(nums)
        for i in range(len(x)):
            if nums.count(x[i]) >= len(nums) // 2:
                return i