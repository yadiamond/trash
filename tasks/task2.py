#task: https://leetcode.com/problems/length-of-last-word/
def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    return len(s.split()[-1])