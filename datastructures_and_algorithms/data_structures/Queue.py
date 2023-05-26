# queue1 = []
#
# queue1.append(1)
# queue1.append(6)
# queue1.append(7)
# queue1.append(15)
#
# print(queue1)
#
# queue1.pop(0)
# print(queue1)


# or we can define class queue

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


# enqueue()
q = Queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(10)
q.enqueue(15)
print(q)

# # dequeue()
q.dequeue()
print(q)


