from collections import deque
import time
import threading

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


# Food ordering system
orders = ["pizza", "samosa", "pasta", "biryani", "burger"]
queue = Queue()

# Place order every 0.5 second
def place_order(orders):
    for order in orders:
        print(f"{order} has been ordered.")
        queue.enqueue(order)
        time.sleep(0.5)


# Serve order every 2 seconds
def serve_order():
    time.sleep(1)
    while queue.size() > 0:
        served = queue.dequeue()
        print(f"{served} has been served.")
        time.sleep(2)


t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order, args=())

t1.start()
t2.start()
