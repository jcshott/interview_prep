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

def reverse_string(astring):
	"""use recursion to reverse a string"""

	if len(astring) < 1:
		return astring
	else:
		return reverse_string(astring[1:]) + astring[0]

print reverse_string("joy")
print reverse_string("Corey")
print reverse_string("Ruby Roo")

def is_pal(s):
	"""checks whether something is a palindrome using recursion. 
	takes a string of all alpha numeric characters (no whitespace or special chars in same case)
	returns True if is a palindrome, False if not.
	could use helper functions if wanted to take other types of strings (i.e. phrases or upper/lower combinations"""

	if len(s) < 2:
		return True
	else:
		return is_pal(s[1:-1]) and s[0] == s[-1]
	return False

print is_pal("radar")
print is_pal("corey")
print is_pal("abdccdba")
print is_pal("ruby")


def factorial_recursive(num):
	if num == 1 or num == 2:
		return num
	else:
		return factorial_recursive(num-1) * num

print factorial_recursive(5)
print factorial_recursive(1)
