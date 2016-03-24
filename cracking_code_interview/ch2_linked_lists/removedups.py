from linkedList import Node, LinkedList

def remove_dups(ll):
	"""remove duplicate nodes from an unsorted linked list"""

	nodes_seen = {}
	previous = None
	current = ll.head


	while current:
		# check to see if in tracking dict. if so, this is a duplicate
		if nodes_seen.get(current.data, None):
			# remove the node
			if current.next == None: #check if we are on last node
				previous.next = None
			else:
				current.data = current.next.data
				current.next = current.next.next
			
			# move to next
			previous = current
			current = current.next
		# if not in dict - this isn't a dup. add it to dict and move on
		else:
			nodes_seen.setdefault(current.data, True)
			previous = current
			current = current.next

	return ll

my_list = LinkedList(Node(2, Node(4, Node(1, Node(2, Node(7, Node(1)))))))
print "testing having to remove last node"
print "my_list before: ", my_list.as_string()
remove_dups(my_list)
print "my_list after: ", my_list.as_string()

print "testing not having to remove last node: "

another_list = LinkedList(Node(4, Node(4, Node(1, Node(2, Node(7))))))

print "another_list before: ", another_list.as_string()
remove_dups(another_list)
print "another_list after: ", another_list.as_string()
