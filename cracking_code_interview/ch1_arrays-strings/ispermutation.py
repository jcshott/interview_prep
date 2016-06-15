def is_permutation(str1, str2):
	""" check if one string is a permutation of another """

	char_a = {}
	char_b = {}

	for a in str1:
		char_a[a] = char_a.get(a, 0) + 1

	for b in str2:
		char_b[b] = char_b.get(b, 0) + 1

	return char_a == char_b

assert is_permutation("aabbcda", "cdababa") == True

assert is_permutation("xyz", "aabbcda") == False

assert is_permutation("abbc", "aabbcda") == False
