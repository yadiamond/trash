#task: https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums):
        proceed = []
        for i in nums:
            if i in proceed:
                proceed.remove(i)
            else:
                proceed += [i]
        return proceed[0]