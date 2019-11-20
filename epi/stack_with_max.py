class StackWithMax:

    def __init__(self):
        self.normal_stack = []
        self.max_stack = []

    def push(self, i):
        if len(self.max_stack) == 0 or i >= self.max_stack[-1]:
            self.max_stack.append(i)
        self.normal_stack.append(i)

    def pop(self):
        i = self.normal_stack.pop()
        if i == self.max_stack[-1]:
            self.max_stack.pop()
        return i

    def max(self):
        return self.max_stack[-1]
