#task: https://leetcode.com/problems/add-binary/
def addBinary(a, b):
    ax = 0
    for index, val in enumerate(reversed(a)):
        ax += int(val) * (2 ** index)
    
    bx = 0
    for index, val in enumerate(reversed(b)):
        bx += int(val) * (2 ** index)
    return bin(ax + bx)[2:]