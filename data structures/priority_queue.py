class PriorityQueue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        if len(self.queue) == 0:
            self.queue.append((item, priority))
        else:
            for i in range(len(self.queue)):
                for j in range(len(self.queue)):
                    if self.queue[i][1] <= self.queue[j][1]:
                        continue
                    else:
                        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed[0]
    
s = PriorityQueue()
s.enqueue(3, 3)
s.enqueue(5, 5)
s.enqueue(1, 1)
print(s.queue)