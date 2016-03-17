from is_substring import is_substring

def is_rotation(s1, s2):
	""" checks whether string 2 (s2) is a rotation of string 1 (s1) 
	using only 1 call to is_substring"""

	# we concat one string because if s2 is a rotation of s1, 
	# this will "remake" or "reconstitute" s2 in the middle of check_string
	check_string = s1 + s1

	return is_substring(check_string, s2)

assert is_rotation("erbottlewat", "waterbottle") == True
assert is_rotation("waterbottle", "botwater") == False