# given input of string, list or num, output the string JSON representation
# ex
# input: 5 => "5"
# input: "hello" => "\"hello\""
# input: [5, "hello"] => "[5, \"hello\"]"

def process_list(lst):
	out = "["
	for item in lst:
		if type(item) == int:
			out += str(item) + ", "
		elif type(item) == str:
			out += "\"" + item + "\"" + ", "
	out = out.rstrip(", ")
	return out + "]"

def json_rep(my_obj):
	if type(my_obj) == int:
		return str(my_obj)
	if type(my_obj) == str:
		return "\"" + my_obj + "\""
	if type(my_obj) == list:
		# return str(my_obj)
		out = []
		# out = "["
		for item in my_obj:
			if type(item) == int:
				out.append(str(item))
			elif type(item) == str:
				out.append("\"" + item + "\"")
			elif type(item) == list:
				out.append(process_list(item))
		
		out = ", ".join(out)
		return "[" + out + "]"

print json_rep(5)
print json_rep("hello")
test_lst = json_rep([5, "hello"])
print "type test_lst: ", type(test_lst)
print "output of test_lst: ", test_lst
test_lst_with_sublists = json_rep([7, "ruby", "rocky", [10, 5], ["yo"]])
print "type test_lst_with_sublists: ", type(test_lst_with_sublists)
print "output of test_lst_with_sublists: ", test_lst_with_sublists