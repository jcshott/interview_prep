def is_substring(str1, str2):
	""" check if one string is a substring of another """

	# find the shorter string, which we will set to 'a' and longer is 'b'
	a = ""
	b = ""

	if len(str1) <= len(str2):
		a = str1
		b = str2
	else:
		a = str2
		b = str1

	# we only want to evaluate the b string while it's long enough to contain the a string
	while len(b) >= len(a):
		# if we find a match, break & return true
		if b[:len(a)] == a:
			return True
		# otherwise, cut the b string down by one and eval the next set of a-length strings
		else:
			b = b[1:]
	# if we get to where the bstring is shorter than the a string and haven't founda match, there is no match
	return False

assert is_substring("aabbcda", "cda") == True

assert is_substring("xyz", "aabbcda") == False
