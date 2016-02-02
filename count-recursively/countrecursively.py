"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""


def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if not lst:
    	return 0
    else:
    	count = count_recursively(lst[1:]) + 1
    	# could just return count_recursively(lst[1:]) + 1 but this way you can do print stmts to see what is happening if needed
    	return count

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"
