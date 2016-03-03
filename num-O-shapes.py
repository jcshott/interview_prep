def num_o_shapes(mystr):
	shape_dict = {
	"A": 1, "B": 2, "D": 1, "O": 1, "R": 1, "P": 1, "Q": 1, "R": 1, "a": 1, "b": 1, "d": 1,
	"e": 1, "g": 1, "o": 1, "p": 1, "q": 1, "4": 1, "6": 1, "8": 2, "9": 1, "0": 1}
	
	total = 0
	
	for char in mystr:
		num = shape_dict.get(char, 0)
		total += num

	return total

print num_o_shapes("ate")
print num_o_shapes("1ft")