# create a function def parse_csv(text): that will parse and print the CSV, 
# there may be trailing white spaces and quotes ("") can be used to escape commas.
####
# get the text
# check for a comma
# if comma has "" on either side, ignore
# otherwise, print everything before and up to the comma

def parse_csv(text):
	# keep track of beginning of "print" and an idx that moves
	beg_idx = 0
	curr_idx = 0

	while curr_idx < len(text):
		if text[curr_idx] == ",":
			# if we've escaped
			if text[curr_idx-1] == "\"" and text[curr_idx+1] == "\"":
				curr_idx += 1
			else:
				# replace any escaped commas you found with a comma
				out = text[beg_idx:curr_idx].replace("\",\"", ",")
				print out.strip()
				# move the beg_index to one past the current(aka the comma)
				beg_idx = curr_idx+1
				curr_idx = beg_idx
		else:
			curr_idx += 1

	out = text[beg_idx:].replace("\",\"", ",")
	print out.strip()

if __name__ == '__main__':
	f_info = open("test.csv")

	parse_csv(f_info.read())
	# parse_csv("rocky,ruby\",\"dog")