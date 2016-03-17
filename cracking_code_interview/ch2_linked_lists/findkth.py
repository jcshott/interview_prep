from linkedList import Node

def find_kth_node(linkedlist, k):
	""" return the kth to last node in a singly linked list"""

	b = linkedlist
	a = linkedlist

	count = 0

	while count != k and a.next:
		a = a.next
		count += 1

	if not a.next:
		return "too short to return the %dth value" %k

	while a.next:
		b = b.next
		a = a.next

	return b

my_ll = Node(2, Node(5, Node(1, Node(7, Node(8)))))

my_found_node = find_kth_node(my_ll, 2)
print my_found_node.data

my_bad_ll = Node(2, Node(5))

my_not_node = find_kth_node(my_bad_ll, 2)
print my_not_node

find_last_node = find_kth_node(my_ll, 0)
print find_last_node.data