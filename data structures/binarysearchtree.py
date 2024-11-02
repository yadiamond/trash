class TreeNode():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class BinaryTree():
    def __init__(self, root):
        self.root = TreeNode(root)
    
    def append(self, item):
        newnode = TreeNode(item)
        lastbox = self.root
        while lastbox is not None:
            if newnode.value > lastbox.value:
                if lastbox.right is None:
                    lastbox.right = newnode
                else:
                    lastbox = lastbox.right
            else:
                if lastbox.left is None:
                    lastbox.left = newnode
                else:
                    lastbox = lastbox.right

