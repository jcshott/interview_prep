class Stack(object):
	""" Stack: Last-In, First Out """

	def __init__(self, inList=[]):
		self.items = inList

	def push(self, item):
		""" add item to stack, returns nothing """

		self.items.append(item)

	def pop(self):
		""" returns most recently added item & removes from stack """
		try:
			return self.items.pop()
		except IndexError:
			return None
		
	def peek(self):
		""" returns most recently added item, doesn't change stack """
		try:
			return self.items[-1]
		except IndexError:
			return None
		
	def isEmpty(self):
		""" returns True/False """

		return len(self.items) == 0


