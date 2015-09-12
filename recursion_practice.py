def len_list (list):

	if not list:
		return 0
	
	return 1 + len_list(list[1:])

print len_list([7, 8, 5, 8])


#first time through list is all (a)
#then we call it on [8, 5, 8] (b)
#then call on [5, 8] (c)
#then call on [8] (d)
#then call on [] (e) so break out and return 0 which is returned to the 1 + 0 (d)
#that is returned up to another 1 + 1 = 2 (c)
#that is returned up to another 1 + 2 = 3 (b)
#that is returned up to another 1 + 3 (a)