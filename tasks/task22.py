#task: https://leetcode.com/problems/symmetric-tree/
class Solution:
    def isSymmetric(self, root):
        l = root.left
        r = root.right
        Solution.func(l, r)
    
    def func(l, r):
        if l is None and r is None:
            return True
        elif l.val == r.val:
            return func(l.left, r.right) & func(l.right, r.left)
        else:
            return False