def fibonnacci(n):
	"""
	fibonnacci sequence is 1, 1, 2, 3, 5....etc.

	input: n-integer
	output: the n'th fibonnacci number (i.e. n=3; output=2 )

	>>> fibonnacci(5)
	5

	>>> fibonnacci(1)
	1

	>>> fibonnacci(7)
	13

	>>> fibonnacci(2)
	1

	"""
	### iterative
	fib_1 = 1
	fib_2 = 1

	if n <= 2:
		return 1

	for x in xrange(2, n):
		fib_1, fib_2 = fib_2, fib_1+fib_2

	return fib_2

	### recursive
		# base case is less than or equal to 2 because both fib(1) & fib(2) are 1
	# if n <= 2:
	# 	return 1

	# return fibonnacci(n-1) + fibonnacci(n-2)


if __name__ == '__main__':
	import doctest

	if doctest.testmod().failed == 0:
		print "\n*** ALL TESTS PASSED.\n"
