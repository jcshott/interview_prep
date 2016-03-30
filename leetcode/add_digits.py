def add_digits(num):
	""" Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

	For example:

	Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
	>>> add_digits(38)
	2

	>>> add_digits(12)
	3

	>>> add_digits(795)
	3

	"""

	a = num/10
	b = num % 10
	c = a + b

	if c < 10:
		return c

	return add_digits(c)

if __name__ == '__main__':
	import doctest

	if doctest.testmod().failed == 0:
		print "Tests passed!"