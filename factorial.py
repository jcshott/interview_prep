"""Write a recursive and iterative solution for a finding the factorial of a number. 
If you don't remember, the factorial of a non-negative integer n, denoted n! is the 
product of all positive integers less than . For example, 5! = 5 * 4 * 3 * 2 * 1

"""

def factorial_rec(n):
	"""takes an integer as argument
	returns n!
	using recurision

		>>> factorial_rec(5)
		120
		>>> factorial_rec(1)
		1

	"""

	if n == 1:
		return n
	else:
		x = factorial_rec(n-1)
		return n * x


def factorial_iterative(n):
	"""itertive solution

		>>> factorial_iterative(5)
		120
		>>> factorial_iterative(7)
		5040

	"""

	out = 1

	for x in range(1, n+1):
		out*=x
	return out


if __name__ == '__main__':
	import doctest

	result = doctest.testmod()
	if not result.failed:
		print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted