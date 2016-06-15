
def json_rep_rec(obj):
	
	def _json_to_rep_rec(my_obj, lst):
		if type(my_obj) == int or type(my_obj) == float:
			return str(my_obj)
		if type(my_obj) == str:
			return "\"" + my_obj + "\""
		
		if type(my_obj) == list:
			if len(my_obj) == 1:
				return _json_to_rep_rec(my_obj[0])
			x = _json_to_rep_rec(my_obj[1:])
		

		# return _json_rep_rec(my_obj[1:]) # x = "hello"
	
	# if type(my_obj) == int or type(my_obj) == float:
	# 		return str(my_obj)
	
	# if type(my_obj) == str:
	# 		return "\"" + my_obj + "\""
	x = _json_to_rep_rec(obj)
	out.append(x)
	print out

json_rep_rec([5, "test", 7])


