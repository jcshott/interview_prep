def recursive_search(needle, haystack, idx=0):
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
	# def _recursive_haystack(needle, haystack, idx=0):
	# 	# if the index is equal to len of haystack, then we've gone thru haystack & needle not there
	# 	if idx == len(haystack):
	# 		return None
	# 	# if the haystack item at index is the needle. we found it, return that index
	# 	if haystack[idx] == needle:
	# 		return idx
	# 	# if we haven't found it, go to next index
	# 	return _recursive_haystack(needle, haystack, idx+1)
	# # call the recursive function with a new variable, indx starting at zero
	# return _recursive_haystack(needle, haystack, 0)
	if idx == len(haystack):
		return None
	if haystack[idx] == needle:
		return idx
	return recursive_search(needle, haystack, idx+1)

if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
