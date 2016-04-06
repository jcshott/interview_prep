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
		if curr_idx == 0 and text[curr_idx] == "\"":
			quote = True
			curr_idx += 1
		# if we see a quote, we need to ignore commas until we see another so set to True
		elif text[curr_idx] == "\"" and text[curr_idx-1] != "\\" and not quote:
			quote = True
			curr_idx += 1
		# if we've seen a quote already, we have our second "escape" quote so return to false so we catch next comma as seperator
		elif text[curr_idx] == "\"" and text[curr_idx-1] != "\\" and quote:
			quote = False
			curr_idx +=1
		elif text[curr_idx] == "\"" and text[curr_idx-1] == "\\":
			curr_idx += 1

		# if we hit a comma and we don't have a quote/it's not within an escape, print the string so far
		elif text[curr_idx] == "," and not quote:
			# strip whitespace and extra quotes first then get rid of escape symbol and turn escaped comma into simple comma
			print text[beg_idx:curr_idx].strip().strip("\"").replace("\\", "").replace("\",\"", ",")
			beg_idx = curr_idx+1
			curr_idx = beg_idx
		
		elif text[curr_idx] == "," and quote:
			curr_idx += 1
		else:
			curr_idx += 1

	print text[beg_idx:].strip().strip("\"").replace("\\", "").replace("\",\"", ",")

if __name__ == '__main__':
	## my example input: 
	# parse, all, the things
	# rocky, ruby","dog,"one,two",yes
	# A, "B,C", "D\",", E
	# "\"G, H", l, m\"

	# my understand of what the output in terminal should be:
	# parse
	# all
	# the things
	# rocky
	# ruby,dog
	# one,two
	# yes
	# A
	# B,C
	# D",
	# E
	# "G, H
	# l
	# m

	f_info = open("test.csv")
	
	for line in f_info:
		parse_csv(line)
