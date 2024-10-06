class Box():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def containing(self, item):
        lastbox = self.head
        while lastbox:
            if item == lastbox.data:
                return True
            else:
                lastbox = lastbox.next
            return False
    
    def append(self, item):
        newbox = Box(item)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head 
        while lastbox.next:
            lastbox.next
        lastbox.next = newbox
        
    def get(self, index):
        lastbox = self.head
        boxindex = 0
        while boxindex <= index:
            if boxindex == index:
                return lastbox.data
            boxindex += 1
            lastbox = lastbox.next
    
    def remove(self, item):
        head = self.head
        if head is not None:
            if head.data == item:
                self.head = head.next
                head = None
                return
            while head is not None:
                if head.data == item:
                    break
                lastbox = head
                head = head.next
            if head == None:
                return
            lastbox.next = head.next
            head = None
            