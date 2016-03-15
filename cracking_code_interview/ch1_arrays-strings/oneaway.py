def is_one_away(s1, s2):
	""" checks if strings are only one change away. 

		change defined as 1 char added, removed or changed
	"""
	# quick check to see if the lengths vary by more than 1 char, quick exit if so.
	if abs(len(s1) - len(s2)) > 1:
		return False

	# keep track if we've seen an edit made
	edit = False
	string_a = "" # shortest string
	string_b = "" # longest string
	
	# seperate indices in case we have edit in middle
	idx_a = 0
	idx_b = 0

	# set string_a & string_b to shortest, longest strings
	if len(s1) <= len(s2):
		string_a = s1
		string_b = s2
	else:
		string_a = s2
		string_b = s1
	
	# go through until we hit length of longest string.
	# we've already checked that they are only 1 char apart.

	while idx_a < len(string_a) and idx_b < len(string_b):
		if string_a[idx_a] != string_b[idx_b]: # if we hit a difference, make sure it's first one.
			if edit:
				return False
			edit = True # if its the first one, make sure we keep track of that

			if len(string_a) < len(string_b): # if our lengths are different, we have to keep track of the indices at diff rates
				idx_b += 1
			else:
				idx_a += 1
				idx_b += 1
		else:
			# if the chars at indice match, just increment.
			idx_a += 1
			idx_b +=1


	return True

assert is_one_away("pale", "ple") == True
assert is_one_away("pales", "pale") == True
assert is_one_away("pale", "bale") == True
assert is_one_away("pale", "bae") == False
assert is_one_away("dog", "yo mamma") == False

print is_one_away("pale", "bale")