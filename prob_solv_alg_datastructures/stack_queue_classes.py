class Stack(object):

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def is_Empty(self):
		return self.items == []

	def size(self):
		return len(self.items)


class Queue(object):

	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def is_Empty(self):
		return self.items == []

class Deque(object):
	"""Double-ended Queue class"""

	def __init__(self):
		self.items = []

	def add_front(self, item):
		self.items.append(item)

	def add_back(self, item):
		self.items.insert(0, item)

	def remove_front(self):
		return self.items.pop()

	def remove_back(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

	def is_Empty(self):
		return self.items == []


	




