class Stack():
    
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed
s = Stack()
s.push(13)
s.push(1)
s.push(2)
s.push(3)
s1 = s.pop()
print(s.stack, s1)