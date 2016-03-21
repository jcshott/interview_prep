from linkedList import Node

def partition(ll, x):
	""" write code to partition a LL around a value x, 
	such that all nodes less than x come before all nodes greater than or equal to x.
	if x is in the list, values of x only need to be after elements less than x

	ex.

	input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 
	[partition = 5]

	output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8 (or similar, order within greater or lesser doesn't matter)

	"""

	# create list of all nodes >= to partition value 

	move_list = []

	# go through our LL and take out the nodes >= and add to our move_list

	current = ll

	while current:
		if current.data >= x:
			move_node = Node(current.data)
			move_list.append(move_node)
			current.data = current.next.data
			current.next = current.next.next
		else:
			current = current.next

	for n in move_list:
		ll.add_node(n)

my_ll = Node(3, Node(5, Node(8, Node(5, Node(9, Node(2, Node(1)))))))

print my_ll.as_string()

partition(my_ll, 5)

print my_ll.as_string()