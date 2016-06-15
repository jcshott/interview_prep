def magic_index_recursion(array):
	""" magic index is defined as given array A, if A[i] == i, return True
	input: sorted array of distinct integers
	ouput: true/false if there is a magic index

	"""

	def _magic_idx(array, idx):

		"""since we are only given a sorted array in problem,
		define recursive function to call, adding idx counter
		"""

		if idx == len(array):
			# we've gone too far and haven't found a magic index
			return False

		if array[idx] == idx:
			# yay, we found one!
			return True

		return _magic_idx(array, idx+1)

	return _magic_idx(array, 0)


def magic_idx_pythonic(array):

	for idx, val in enumerate(array):
		if idx == val:
			return True
	return False

print "[1, 2, 3, 3, 5, 8]"
print "recursion version: ", magic_index_recursion([1, 2, 3, 3, 5, 8])
print "pythonic version: ", magic_idx_pythonic([1, 2, 3, 3, 5, 8])

print "[1, 2, 3, 4, 5, 6, 7]"
print "recursion version: ", magic_index_recursion([1, 2, 3, 4, 5, 6, 7])
print "pythonic version: ", magic_idx_pythonic([1, 2, 3, 4, 5, 6, 7])
