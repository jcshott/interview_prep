"""  
Hacker Rank: Sherlock & the Beast

Find the largest Decent Number having N digits.

A Decent Number has the following properties:

Its digits can only be 3's and/or 5's.
The number of 3's it contains is divisible by 5.
The number of 5's it contains is divisible by 3.
If there are more than one such number, we pick the largest one.

Input Format:

The first line is an integer, T, denoting the number of test cases.

The T subsequent lines each contain an integer, N, detailing the number of digits in the number.

Output Format:

Print the largest Decent Number having N digits; if no such number exists, tell Sherlock by printing -1.
"""

def main(num_digits):

	# keep track of how many digits we have left to fill
	digits_left = num_digits
	
	# can we fill all remaining digits with 5s (i.e. is it evenly div by 3?)
	while digits_left%3 != 0:
		# if not, then take out 5 digits => one "set" of 3s to fill-in.
		digits_left -= 5
		# take out the number of "sets" of 3s until you have a number divisible by 3

	# if you get to the point were you can't have even number of 3s or 5s. that's a bad dig num
	if digits_left < 0:
		return "-1"
	
	# otherwise, print out the number of sets of 5 remaining + how many sets of 3 you took out
	else:
		return digits_left*'5' + (num_digits-digits_left)*'3'

if __name__ == "__main__":
	## for HR system
	# t = int(raw_input().strip())
	# for a0 in xrange(t):
	    # n = int(raw_input().strip())
		# print main(n)
	assert main(1) == "-1"
	assert main(3) == "555"
	assert main(5) == "33333"
	assert main(11) == "55555533333"
	# make sure it's highest possible which is with 5s first
	assert main(13) != "3333333333555"