class Box():
    def __init__(self, data = None):
        self.data = data
        self.previous = None
        self.next = None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
    
    def append(self, item):
        newbox = Box(item)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while lastbox.next:
            lastbox = lastbox.next
        lastbox.next = newbox
        newbox.previous = lastbox

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
        if head.data is not None:
            if head.data == item:
                self.head = head.next
                self.head.previous = None
                return
            while head is not None:
                if head.data == item:
                    break
                lastbox = head
                head = head.next
            if head == None:
                return
            lastbox.next = head
            head.previous = lastbox
            head = None