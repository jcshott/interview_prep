class Node(object):
	"""defines attributes and methods for linked list node"""

	def __init__(self, init_data):
		self.data = init_data
		self.next = None


class LinkedList(object):
	"""defines attributes and methods for linked list class"""

	def __init__(self, head=None):
		self.head = head

	def add(self, item):
		"""adds a node at BEGINNING of LL.  No return value"""
		temp = Node(item)
		temp.next = self.head
		self.head = temp

	def append(self, item):
		"""adds a node at END of LL. No return value"""

		temp = Node(item)
		current = self.head

		while current.next != None:
			current = current.next
		current.next = temp
	
	def search(self, value):
		"""search for given value in LL. returns True or False depending on if value found"""
		current = self.head

		while current != None:
			if current.data == value:
				return True
			else:
				current = current.next

		return False

	def size(self):
		"""returns number of nodes in linked list"""
		current = self.head
		count = 0

		while current != None:
			count += 1
			current = current.next
		return count

	def remove(self, item):
		"""removes node with given item value from linked list. returns nothing"""

		current = self.head
		previous = None

		while current.data != item:
			previous = current
			current = current.next

		if previous == None:
			self.head = current.next
		else:
			previous.next = current.next
