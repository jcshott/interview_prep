def fib_nums(n):

	""" return n number of fibonacci numbers.  fib nums = 1, 1, 2, 3, 5, 8....
	>>> fib_nums(4)
	3
	>>> fib_nums(2)
	1
	>>> fib_nums(6)
	8

	"""
	### loop answer -> O(N) because just checking and looping
	# if n <= 0:
	# 	return "greater than zero, please"
	
	# if n <= 2:
	# 	return 1
	
	# else:
	# 	x = 1
	# 	y = 1
	# 	z = 0
		
	# 	for i in range(n-2):
	# 		z = x + y
	# 		x = y
	# 		y = z

	# 	return z

	### Recursion answer.  much higher O(N) runtime

	if n <= 2:
		return 1

	return fib_nums(n-1) + fib_nums(n-2)

if __name__ == '__main__':
	import doctest

	if doctest.testmod().failed == 0:
		print "boom"