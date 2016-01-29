def rev_string(mystring):
	i = 0
	j = -1
	str_list = list(mystring)
	
	while i < len(str_list)/2:
		str_list[i], str_list[j] = str_list[j], str_list[i]
		i += 1
		j -= 1
	
	return "".join(str_list)

print rev_string("dog")
print rev_string("apple")
print rev_string("ruby")

def rev_string_list(mystring):
	letter_lst = []

	for x in mystring:
		letter_lst.append(x)

	out_str = ""
	
	while letter_lst:
		out_str = out_str + letter_lst.pop()

	return out_str

print rev_string_list("dog")
print rev_string_list("apple")
print rev_string_list("ruby")

def reverse_string_recursion(astring):
	"""use recursion to reverse a string"""

	if len(astring) < 1:
		return astring
	else:
		return reverse_string_recursion(astring[1:]) + astring[0]

print reverse_string_recursion("joy")
print reverse_string_recursion("Corey")
print reverse_string_recursion("Ruby Roo")