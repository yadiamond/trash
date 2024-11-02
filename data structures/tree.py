class TreeNode():
    def __init__(self, item):
        self.item = item
        self.children = []
        
    def append(self, item):
        self.children.append(item)