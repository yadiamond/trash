#task: https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root):
        return func(1, head)
    def func(i, head):
        if head is None:
            return i - 1
        else:
            if head.right is None and head.left is None:
                return i
            else:
                return max(func(i + 1, head.right), func(i + 1, head.left))