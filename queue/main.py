# Not best approach because of data allocation
wmt_stock_prices_queue = []

wmt_stock_prices_queue.insert(0, 131.10)
wmt_stock_prices_queue.insert(0, 132.12)
wmt_stock_prices_queue.insert(0, 135)

wmt_stock_prices_queue.pop()
wmt_stock_prices_queue.pop()


# Recommended approach
from collections import deque

q = deque()
q.appendleft(5)
q.appendleft(10)
q.appendleft(39)

q.pop()


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


pq = Queue()

pq.enqueue({"company": "WalMart", "timestamp": "15 apr, 11.01 AM", "price": 131.10})

pq.enqueue({"company": "WalMart", "timestamp": "15 apr, 11.02 AM", "price": 132})

pq.enqueue({"company": "WalMart", "timestamp": "15 apr, 11.03 AM", "price": 135})

print(pq.buffer)

print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
