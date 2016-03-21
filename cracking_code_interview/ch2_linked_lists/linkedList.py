class Node(object):
	""" class for a node in a linked list """

	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def as_string(self):
		"""Represent data for this node and it's successors as a string.

		>>> Node(3).as_string()
		'3'

		>>> Node(3, Node(2, Node(1))).as_string()
		'321'
		"""

		out = []
		n = self
		
		while n:
			out.append(str(n.data))
			n = n.next

		return "".join(out)

	def add_node(self, node):

		current = self

		while current.next:
			current = current.next

		current.next = node

	def remove_node(self, data):

		if self.data == data:
			self.data = self.next.data
			self.next = self.next.next

		else:	
			current = self
			
			while current.next.data != data:
				current = current.next
			if current.next:
				current.next = current.next.next
			else:
				return "node not found"

def test_methods():
	print "add: "
	test = Node(1, Node(2))
	print test.as_string()

	test.add_node(Node(3))
	print test.as_string()

	print "remove: "
	test.remove_node(3)
	print test.as_string()

	print "remove from front: "
	test2 = Node(2, Node(1, Node(3)))
	print test2.as_string()
	test2.remove_node(2)
	print test2.as_string()

	
if __name__ == '__main__':
	test_methods()

