class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
x = queue.dequeue()
print(queue.queue, x)