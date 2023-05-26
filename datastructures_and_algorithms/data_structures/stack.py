# stack1 = [7, 16, 45, 25]
#
# stack1.append(1)
# stack1.append(5)
#
# print(stack1)
#
# stack1.pop()
# print(stack1)


# defining class stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) < 1:
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


# push()
s = Stack()
s.push(5)
s.push(8)
s.push(15)
s.push(25)

print(s)

# pop()
s.pop()
print(s)
