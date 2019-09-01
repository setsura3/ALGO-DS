
class Queue():
    def __init__(self):
        self.ele = []

    def enqueue(self, ele):
        self.ele.append(ele)

    def dequeue(self):
        return self.ele.pop(0)

    def getQueue(self):
        return self.ele

    def getSize(self):
        return len(self.ele)

    def isEmpty(self):
        return self.ele == []

    def getFirst(self):
        return self.ele[0]
