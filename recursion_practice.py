def len_list (list):

	if not list:
		return 0
	
	print len(list)
	
	return 1 + len_list(list[1:])

print len_list([7, 8, 5, 8])


