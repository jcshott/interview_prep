def urlify(astring):
	""" input: string
		output: string with spaces replaced by "%20"
	"""

	word_list = astring.split(" ")
	return "%20".join(word_list)

assert urlify("John Doe") == "John%20Doe"

assert urlify("test") == "test"