#task: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        mid = len(nums) // 2
        head = TreeNode(nums[mid])
        root = head
        Solution.func(nums, head)
        return root
    def func(nums, head):
        mid = len(nums) // 2
        low = nums[:mid]
        high = nums[mid + 1:]
        midl = len(low) // 2
        midh = len(high) // 2
        if high == []:
            if low == []:
                pass
            else:
                head.left = TreeNode(low[0])
        else:
            head.left = TreeNode(low[midl])
            head.right = TreeNode(high[midh])
            Solution.func(low, head.left)
            Solution.func(high, head.right)
        