from collections import deque
import time

# Building a Queue Class
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


queue = Queue()
maxNum = 10


def binary_nums(maxNum):
    while maxNum > 0:
        if queue.is_empty():
            queue.enqueue(1)
            maxNum -= 1
        else:
            current_num = queue.front()
            if maxNum > 0:
                queue.enqueue(int(f"{current_num}0"))
                maxNum -= 1
            if maxNum > 0:
                queue.enqueue(int(f"{current_num}1"))
                maxNum -= 1
            removed_num = queue.dequeue()
            print(removed_num)

    while queue.size() > 0:
        removed_num = queue.dequeue()
        print(removed_num)


binary_nums(maxNum)
