def recursive_search(needle, haystack):
	"""Given list (haystack), return index (0-based) of needle in the list.

	Return None if needle is not in haystack.
	
	Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
	
	>>> lst = ["hey", "there", "you"]
	>>> recursive_search("hey", lst)
	0
	>>> recursive_search("you", lst)
	2
	
	>>> recursive_search("porcupine", lst) is None
	True
	
	"""

	def _recursive_search(needle, haystack, seen=0):

		if seen == len(haystack):
			return None

		if haystack[seen] == needle:
			return seen

		return _recursive_search(needle, haystack, seen+1)

	return _recursive_search(needle, haystack, 0)




if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
