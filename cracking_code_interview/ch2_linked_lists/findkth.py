from linkedList import Node, LinkedList

def find_kth_to_last_node(linkedlist, k):
	""" return the kth to last node in a singly linked list"""

	b = linkedlist.head
	a = linkedlist.head

	count = 0

	while count != k and a.next:
		a = a.next
		count += 1

	if not a.next:
		return "too short to return the %d to last value" %k

	while a.next:
		b = b.next
		a = a.next

	return b

my_ll = LinkedList(Node(2, Node(5, Node(1, Node(7, Node(8))))))

my_found_node = find_kth_to_last_node(my_ll, 2)
print my_found_node.data

my_bad_ll = LinkedList(Node(2, Node(5)))

my_not_node = find_kth_to_last_node(my_bad_ll, 2)
print my_not_node

find_last_node = find_kth_to_last_node(my_ll, 0)
print find_last_node.data