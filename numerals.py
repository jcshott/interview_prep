num_digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def numerals(my_numerals):
	"""convert a string of roman numerals to it's arabic interpretation
	
	>>> numerals("XXX")
	30
	>>> numerals('V')
	5
	>>> numerals("MMMCMXCIX")
	3999
	>>> numerals("MCML")
	1950
	>>> numerals('')
	0
	"""

	eval_str = my_numerals

	total = 0

	while len(eval_str) > 1:
		first_num = num_digit.get(eval_str[0])
		second_num = num_digit.get(eval_str[1])

		if first_num >= second_num:
			total += first_num
			eval_str = eval_str[1:]
		else:
			to_be_added = second_num - first_num
			total += to_be_added
			eval_str = eval_str[2:]

	if eval_str:
		total += num_digit.get(eval_str)
	return total

if __name__ == '__main__':
	import doctest

	if doctest.testmod().failed == 0:
		print "Passed"