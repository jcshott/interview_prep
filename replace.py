def replace(astring, substrings):
	while True:
		to_rem = [i for i in substrings if i in astring]
		if not to_rem:
			return len(astring)
		else:
			for sub in to_rem:
				astring = astring.replace(sub, '')

print replace('ccdaabcdbb', ['ab', 'cd'])