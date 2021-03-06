class loopQueue():
    def __init__(self, capacity):
        self.size = capacity
        self.element = [None] * capacity
        self.head = 0
        self.tail = 0
    def isEmpty(self):
        return self.head == self.tail

    def enqueue(self, ele):
        if self.full():
            print("the queue is full")
            return
        else:
            self.element[self.tail] = ele
            self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.isEmpty():
            print('empty queue')
            return
        else:
            temp = self.element[self.head]
            self.element[self.head] = None
            self.head = (self.head + 1) % self.size
            return temp

    def full(self):
        return (self.tail + 1) % self.size == self.head

    def getQueue(self):
        return self.element

    def getSize(self):
        return self.size
 
