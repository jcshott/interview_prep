def compress_encode(my_string):
	"""
	given a string, output a compressed encryption string.
	ex. 
	>>> astring = "abcccccde"
	>>> compress(astring)
	"ab5xcde"

	"""
	if len(my_string)<= 1:
		return "need a string greater than 1 char"
	
	out = ""
	prev = my_string[0]
	count = 1

	for x in my_string[1:]:
		if x == prev:
			count += 1
			prev = x
		else:
			if count > 1:
				out = out + str(count) + "x" + prev
				count = 1
				prev = x
			else:
				out += prev
				prev = x

	if count == 1:
		out += my_string[-1]
	else:
		out = out + str(count) + "x" + prev
	return out

print compress("abcccccde")
print compress("a2bbAaxyyyy")
print compress("aa")