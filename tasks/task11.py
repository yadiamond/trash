#task: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        ans = head
        while head.next and head:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return ans