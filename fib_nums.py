# def make_fib(N, x=1, y=0):
# 	""" Takes in a number and returns the input (N) number of fibonacci sequence numbers using recursion"""

# 	if N == 0:
# 		return x

# 	else:
# 		print x
# 		make_fib(N-1, x+y, x)

# make_fib(6)

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

print fib(25)

def fib2():
	x = 1
	y = 1
	while x < 25:
		z = x
		x = x+y
		print x
		y = z
	return x

print fib2()
