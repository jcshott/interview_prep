from linkedList import LinkedList, Node

def rev_ll(ll):
	"""
	Returns the head of a new, reversed linked list
	
	"""
	out = None
	curr = ll.head

	while curr:
		out = Node(curr.data, out)
		curr = curr.next

	return out


def is_palindrome(ll):

	orig = ll.head
	rev = rev_ll(ll)

	while orig and rev:
		if orig.data != rev.data:
			return False
		else:
			orig = orig.next
			rev = rev.next
	return True

if __name__ == '__main__':
	
	my_list = LinkedList(Node(2, Node(3, Node(4))))
	print is_palindrome(my_list)

	my_pal_list = LinkedList(Node("a", Node("b", Node("b", Node("a")))))
	print is_palindrome(my_pal_list)
