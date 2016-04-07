"""
	Given a number of objects (say, images), print the ideal number of columns (2-4) to use for 
	arranging on screen:
	ex.
	>>> best_width(2)
	2

	special case that breaks last tie rule
	[] []
	[] []

	>>> best_width(9)
	3

	[] [] []
	[] [] []
	[] [] []

	>>> best_width(8)
	4

	[] [] [] []
	[] [] [] []

	if uneven num, pick the num of rows that gives the most remainder (least hanging in last row)
	
	>>> best_width(11)
	4

	[] [] [] []
	[] [] [] []
	[] [] []

	if tie on remainder (or even), pick most columns

	>>> best_width(13)
	4

	all of col nums (2, 3, 4) have a remainder of 1
	[] [] [] []
	[] [] [] []
	[] [] [] []
	[]

	>>> best_width(12)
	4

	(not 3)
	[] [] [] []
	[] [] [] []
	[] [] [] []


"""
def best_width(n_obj):

	if n_obj > 1:
		# special case - we want 2 columns for 4 items, not 4
		if n_obj == 4:
			return 2
		# store the remainders in logical order 
		# the return value will be the idx + 2 when we find what we want
		remainders = [n_obj%2, n_obj%3, n_obj%4]
		# keep track of the max idx so far
		max_zero_idx = None
		max_remainder = None
		max_rem_idx = None

		# first, check if there is any that are evenly divisible. 
		# we want to grab the highest number of columns we can use so need to iterate through whole list in case of duplicates
		for idx, r in enumerate(remainders):

			if r == 0:
				max_zero_idx = idx
		
		if max_zero_idx >= 0:
			return max_zero_idx + 2
		
		else:
			# find the max remainder, most leftover on incomplete row and the idx of that in our lst
			# if there is a tie, this will return the largest idx (most columns)
			max_rem_idx, max_remainder = max(enumerate(remainders))

			return max_rem_idx + 2
	
	return 1

if __name__ == "__main__":
	import doctest

	if doctest.testmod().failed == 0:
		print "\n*** ALL TESTS PASSED. EXCELLENT!\n"