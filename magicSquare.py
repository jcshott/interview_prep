""" 
started with this question: https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/

A 3x3 magic square is a 3x3 grid of the numbers 1-9 such that each row, column, and major diagonal adds up to 15. Here's an example:
8 1 6
3 5 7
4 9 2
The major diagonals in this example are 8 + 5 + 2 and 6 + 5 + 4. (Magic squares have appeared here on r/dailyprogrammer before, in #65 [Difficult] in 2012.)
Write a function that, given a grid containing the numbers 1-9, determines whether it's a magic square. Use whatever format you want for the grid, such as a 2-dimensional array, or a 1-dimensional array of length 9, or a function that takes 9 arguments. You do not need to parse the grid from the program's input, but you can if you want to. You don't need to check that each of the 9 numbers appears in the grid: assume this to be true.

[8, 1, 6, 3, 5, 7, 4, 9, 2] => true
[2, 7, 6, 9, 5, 1, 4, 3, 8] => true
[3, 5, 7, 8, 1, 6, 4, 9, 2] => false
[8, 1, 6, 7, 5, 3, 4, 9, 2] => false


	EXTENSION: A magic square is an arrangement of the numbers from 1 to N^2 (N-squared) in an NxN matrix, with each number occurring exactly once, and such that the sum of the entries of any row, any column, or any main diagonal is the same.

	DOCTESTS:

	>>> is_magic([8, 1, 6, 3, 5, 7, 4, 9, 2])
	True
	>>> is_magic([2, 7, 6, 9, 5, 1, 4, 3, 8])
	True
	>>> is_magic([7,12,1,14,2,13,8,11,16,3,10,5,9,6,15,4])
	True

	>>> is_magic([3, 5, 7, 8, 1, 6, 4, 9, 2])
	False
	>>> is_magic([8, 1, 6, 7, 5, 3, 4, 9, 2])
	False
"""

# get the input array
# make it a matrix so you can check rows, cols & diags
# if you find one of these isn't 15, return False right away
# if meets all checks, return True, it's magic!
import math

def is_magic(array):

	sub_array_len = int(math.sqrt(len(array)))
	matrix = [array[curr:curr+sub_array_len] for curr in xrange(0, len(array), sub_array_len)]

	# get the sum we need to check against
	target_sum = sum(matrix[0])
	row_len = len(matrix[0])

	# check each row (ea. sub-matrix), if sum is different than target, return right away
	for row in matrix[1:]:
		if sum(row) != target_sum:
			return False

	for col_idx in xrange(row_len):
		total = 0
		# add num at the cell[row_idx][col_idx] (i.e. [0][0]; [1][0]; [2][0]) to total and check all in that col add to target
		for row_idx in xrange(len(matrix)):
			total += matrix[row_idx][col_idx]
		if total != target_sum:
			return False
	
	# check diags
	diag_sum_1 = 0
	diag_sum_2 = 0
	# since we are asssuming a square (NxN) then we can check diags by incrementing both the row & col the same rate and checking the opposite by decrementing the 2nd idx at consistent rate
	for x in xrange(row_len):
		diag_sum_1 += matrix[x][x]
		diag_sum_2 += matrix[x][row_len-(x+1)]

	if diag_sum_1 != target_sum or diag_sum_2 != target_sum:
		return False

	return True

	
if __name__ == "__main__":
	import doctest

	if doctest.testmod().failed == 0:
		print "\n*** ALL TESTS PASSED. EXCELLENT!\n"