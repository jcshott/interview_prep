from linkedList import Node
""" delete a node from a linked list given access only to that node
input: instance of Node() class
output: nothing. changes linked list

"""

def del_mid_node(node):

	if not node.next:
		print "can't delete a tail node"
		return False

	node.data = node.next.data
	node.next = node.next.next
	return True