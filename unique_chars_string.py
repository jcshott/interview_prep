def unique_chars(my_string):
	letter_dict = {}

	for letter in my_string:
		letter_dict.setdefault(letter, 0)
		letter_dict[letter] = letter_dict[letter] + 1

	for letter in my_string:
		num_letters = letter_dict.get(letter)
		if num_letters > 1:
			return False
	return True

print unique_chars('dog')
print unique_chars('abby')
print unique_chars('abhsflvatl')
print unique_chars('')