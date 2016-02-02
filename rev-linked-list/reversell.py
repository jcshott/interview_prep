class Node(object):
    """Class in a linked list."""

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


def reverse_linked_list(head):
    """Given linked list head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
    """

    out_head = None
    n = head

    while n:
        out_head = Node(n.data, out_head)
        n = n.next
    return out_head
    



if __name__ == '__main__':
    
    ll= Node(1, Node(2, Node(3)))
    print reverse_linked_list(ll).as_string()
    print ll.as_string()

    # import doctest
    # if doctest.testmod().failed == 0:
    #     print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
