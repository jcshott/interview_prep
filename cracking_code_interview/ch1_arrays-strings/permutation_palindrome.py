def is_permutation_palindrome (my_string):
	""" input: string
		output: True or False depending on if you can make a palindrome of the letters in string

		for example:
			"Tact Coa" => True ('taco cat', 'acto tca')
	"""
	# make all letters the same case so a 'T' and 't' evaluate as the same char
	astring = my_string.lower()
	chars = {}

	# get all the counts for each letter & store
	for c in astring:
		if c != ' ': #skip spaces
			char_count = chars.get(c, 0)
			chars[c] = char_count + 1

	# we can have only 1 odd count of letters in a palindrome.
	#as soon as we see one, we set this to True
	# can quickly jump out of our function when we see odd count #2
	odd_found = False

	for val in chars.values():
		if val % 2 != 0:
			if odd_found:
				return False
			odd_found = True
	return True


assert is_permutation_palindrome("Tact Coa") == True

assert is_permutation_palindrome("roCky and Ruby") == False
