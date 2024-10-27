#task: https://leetcode.com/problems/plus-one/description/
def plusOne(digits):
    return [int(i) for i in str((int(''.join(map(str, digits))) + 1))]
