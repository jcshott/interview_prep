def make_fib(N, x=1, y=0):
""" Takes in a number and returns the input (N) number of fibonacci sequence numbers """

	if N == 0:
		return x

	else:
		print x
		make_fib(N-1, x+y, x)

make_fib(6)