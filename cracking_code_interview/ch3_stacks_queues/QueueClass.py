class Queue(object):
	""" First-In, First-Out """

	def __init__(self, inList=[]):
		self.items = inList

	def enqueue(self, item):
		""" add item to Queue"""

		self.items.insert(0, item)

	def dequeue(self):
		""" return item at front of Queue & removes from Queue"""
		try:
			return self.items.pop()
		except IndexError:
			return None

	def peek(self):
		"""return item at front of Queue but doesn't change Queue"""
		try:
			return self.items[-1]
		except IndexError:
			return None

	def isEmpty(self):

		return len(self.items) == 0