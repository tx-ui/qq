from multiprocessing import Queue
q = Queue(3)
q.put(1)
q.put(2)
q.put(3)
print(q.full())
# q.put(4)
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())
print(q.empty())

