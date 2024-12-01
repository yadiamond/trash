#task: https://leetcode.com/problems/valid-palindrome/solutions/6051745/video-solution-short-and-simple/
class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        ans = ''
        for i in s:
            if i.isalnum():
                ans += i
        return ans == ans[::-1]
    