def compress(my_str):

	count = 1
	prev = my_str[0]
	out = ""

	for c in my_str[1:]:
		if c == prev:
			count += 1
		else:
			out = out + prev + str(count)
			count = 1
			prev = c
	out = out + prev + str(count)
	if len(out) < len(my_str):
		return out
	return my_str



assert compress("aabcccccaaa") == "a2b1c5a3"
assert compress("aabcccccaab") == "a2b1c5a2b1"
assert compress("aaba") == "aaba"