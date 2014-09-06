import sys

class Stack(object):
    def __init__(self, t):
        self._items = []
        self._index = -1
        self._type = t

    def push(self, item):
        if type(item) is not self._type:
            raise TypeError("Item must be of type {}", t)
        self._items.append(item)
        self._index += 1
        assert self._index == len(self._items) - 1

    def pop(self):
        assert self._index != -1
        temp = self.peek()
        del self._items[self._index]
        self._index -= 1
        return temp

    def peek(self):
        return self._items[self._index]

class LargestStack(Stack):
    def __init__(self, t):
        self._largest = Stack(t)
        self._largest.push(-sys.maxint)
        super(LargestStack, self).__init__(t)

    def push(self, item):
        if item > self._largest.peek():
            self._largest.push(item)
        super(LargestStack, self).push(item)

    def pop(self):
        item = super(LargestStack, self).pop()
        if item == self._largest.peek():
            self._largest.pop()
        return item

    def getLargest(self):
        return self._largest.peek()

def main():
    stack1 = Stack(int)
    stack1.push(2)
    stack1.push(1)
    stack1.push(3)

    lStack1 = LargestStack(int)
    lStack1.push(2)
    lStack1.push(1)
    lStack1.push(3)
    assert lStack1.getLargest() == 3
    assert lStack1.pop() == 3
    assert lStack1.getLargest() == 2

if __name__ == "__main__":
    main()
