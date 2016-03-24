from linkedList import Node, LinkedList
"""
	have two numbers represented by a LL where each node is a digit. 
	digits stored in reverse order such that 1s digit at head
	Function adds the two numbers & returns the sum as a LL (reverese order too)
	ex.
	IN: 7 - 1 - 6 (617) + 5 - 9 - 2 (295)
	OUT: 2 - 1 - 9 (912)
"""
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

def alt_sum_lists(ll_a, ll_b):

	a_curr = ll_a.head
	b_curr = ll_b.head

	sum_ll = LinkedList()

	carryover = 0

	while a_curr or b_curr:
		total = carryover

		if a_curr:
			total += a_curr.data
			a_curr = a_curr.next
		if b_curr:
			total += b_curr.data
			b_curr = b_curr.next

		sum_ll.add_node(Node(total%10))
		carryover = total/10

	if carryover:
		sum_ll.add_node(Node(carryover))
	return sum_ll

if __name__ == '__main__':
	
	a = LinkedList(Node(7, Node(1, Node(6))))
	b = LinkedList(Node(5, Node(9, Node(2))))

	print a.as_string()
	print b.as_string()

	print "adding the lists (617 + 295 = 912) my two ways: "
	print sum_lists(a, b).as_string()

	print alt_sum_lists(a, b).as_string()

	print "uneven lists: 17 + 295 = 312"
	c = LinkedList(Node(7, Node(1)))
	d = LinkedList(Node(5, Node(9, Node(2))))

	print c.as_string()
	print d.as_string()

	print sum_lists(c, d).as_string()
	print alt_sum_lists(c, d).as_string()

	print "one more: 592 + 612 = 1204"
	e = LinkedList(Node(2, Node(9, Node(5))))
	f = LinkedList(Node(2, Node(1, Node(6))))

	print e.as_string()
	print f.as_string()

	print sum_lists(e, f).as_string()
	print alt_sum_lists(e, f).as_string()
