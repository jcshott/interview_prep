from stack_queue_classes import Deque

def palindrome_check(word):
	"""Use deque (double-ended-queue) to check if a word is a palindrome"""

	check_deque = Deque()

	for char in word:
		check_deque.add_front(char)

	while check_deque.size() > 1:
		char_first = check_deque.remove_back()
		char_last = check_deque.remove_front()
		if char_first != char_last:
			return False
	return True

if __name__ == "__main__":

	print "check abba: ", palindrome_check("abba")
	print "check dog: ", palindrome_check("dog")
	print "check racecar: ", palindrome_check("racecar")