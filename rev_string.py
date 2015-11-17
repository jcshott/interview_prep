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