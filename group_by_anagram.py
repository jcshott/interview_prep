def group_anagrams(words):

	anagrams = {}

	for w in words:
		# sort each word because anagrams sorted will be the same so can use as a key
		sorted_w = "".join(sorted(w))
		# value of each sorted w key will be a list of associated words
		anagrams[sorted_w] = anagrams.get(sorted_w, []) + [w]

	return anagrams.values()

def main():
	words = ['dog', 'elvis', 'forest', 'fortes', 'foster', 'goat', 
			'god', 'heros', 'horse', 'lives', 'shore', 'softer']
	expected = [
	['elvis', 'lives'],
	['forest', 'fortes', 'foster', 'softer'],
	['heros', 'horse', 'shore'],
	['dog', 'god'],
	['goat']
	]

	result = group_anagrams(words)
	
	matches = 0

	for x in result:
		for y in expected:
			if set(x) == set(y):
				matches +=1
	print matches == len(result) and matches == len(expected)


if __name__ == "__main__":
	main()