
class MyCircularQueue(object):

    def __init__(self, k):
        self.array = k * [None]
        self.head = 0
        self.tail = -1

    def enQueue(self, value):
        if self.isFull() or value is None:
            return False

        self.advanceTail()
        self.array[self.tail] = value
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.array[self.head] = None
        self.advanceHead()
        return True

    def Front(self):
        if self.isEmpty():
            return -1

        return self.array[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1

        return self.array[self.tail]

    def isEmpty(self):
        if self.isFullOrEmpty():
            return self.array[self.head] is None

    def isFull(self):
        if self.isFullOrEmpty():
            return self.array[self.head] is not None

    def nextPointerPosition(self, pointer):
        pointer += 1
        if pointer >= len(self.array):
            pointer = 0
        return pointer

    def isFullOrEmpty(self):
        return (self.head - self.tail is 1) or (self.tail is len(self.array) - 1 and self.head is 0)

    def advanceTail(self):
        self.tail = self.nextPointerPosition(self.tail)

    def advanceHead(self):
        self.head = self.nextPointerPosition(self.head)
