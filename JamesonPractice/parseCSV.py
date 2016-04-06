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
	quote = False

	while curr_idx < len(text):
		# if we see a quote, we need to ignore commas until we see another so set to True
		if text[curr_idx] == "\"" and not quote:
			quote = True
			curr_idx += 1
		# if we've seen a quote already, we have our second "escape" quote so return to false so we catch next comma as seperator
		elif text[curr_idx] == "\"" and quote:
			quote = False
			curr_idx +=1

		# if we hit a comma and we don't have a quote/it's not within an escape, print the string so far
		elif text[curr_idx] == "," and not quote:
			print text[beg_idx:curr_idx].replace("\",\"", ",").strip().strip("\"")
			beg_idx = curr_idx+1
			curr_idx = beg_idx
		
		elif text[curr_idx] == "," and quote:
				curr_idx += 1
		else:
			curr_idx += 1

	out = text[beg_idx:].replace("\",\"", ",")
	print out.strip()

if __name__ == '__main__':
	## input: 
	#rocky,ruby","dog,"one,two",yes
	#escape, all, the things
	# output in terminal:
		# rocky
		# ruby,dog
		# one,two
		# yes
		# escape
		# all
		# the things

	f_info = open("test.csv")

	parse_csv(f_info.read())
