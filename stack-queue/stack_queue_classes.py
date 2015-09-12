class Stack(object):

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def is_Empty(self):
		return self.items == []

	def size(self):
		return len(self.items)


class Queue(object):

	def __init__(self):
		self.items = ()

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		self.items.pop()
	




