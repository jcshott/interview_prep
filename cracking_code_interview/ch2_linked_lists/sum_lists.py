from linkedList import Node, LinkedList

def sum_lists(ll_a,ll_b):

	a_str = ""
	b_str = ""
	a_curr = ll_a.head
	b_curr = ll_b.head

	while a_curr:
		a_str = str(a_curr.data) + a_str
		a_curr = a_curr.next
	while b_curr:
		b_str = str(b_curr.data) + b_str
		b_curr = b_curr.next

	total = int(a_str) + int(b_str)
	out = LinkedList()

	while total:
		remainder = total % 10
		temp_node = Node(remainder)
		if not out.head:
			out.head = temp_node
		else:
			out.add_node(temp_node)
		total = (total - remainder)/10
	return out

a = LinkedList(Node(7, Node(1, Node(6))))
b = LinkedList(Node(5, Node(9, Node(2))))

print a.as_string()
print b.as_string()

print sum_lists(a, b).as_string()
