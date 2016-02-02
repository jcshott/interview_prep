def product_of_others(array):
	"""takes a list of integers and returns a list of the products of the integers at the other indices
	example:
	>>> nums = [1, 7, 3, 4]
	>>> out = product_of_others(nums)
	>>> out
	[84, 12, 28, 21]

	calculate by [7*3*4, 1*3*4, 1*7*4, 1*7*3]

	"""
	# in this version we are doubling work. each time through we are re-doing some multiplying.
	out_nums = []
	product = 1
	count = 0

	while count != len(array):
		for idx, num in enumerate(array):
			if idx != count:
				product *= num
		
		out_nums.append(product)
		product = 1
		count += 1

	return out_nums

if __name__ == '__main__':
	import doctest

	if doctest.testmod().failed == 0:
		print "\n*** ALL TESTS PASSED. RIGHT ON!\n"



