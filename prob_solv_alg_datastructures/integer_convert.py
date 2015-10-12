from stack_queue_classes import Stack

def convert_integer(decNum, base):
	"""takes in an integer (decimal/base 2) and converts to specified base number"""

	conversion_stack = Stack()
	digits = "0123456789ABCDEF"

	while decNum > 0:
		remainder = decNum % base
		conversion_stack.push(remainder)
		decNum = decNum / base

	out_string = ""
	
	while not conversion_stack.is_Empty():
		out_string = out_string + digits[conversion_stack.pop()]

	return out_string

print convert_integer(25, 8)
print convert_integer(256, 16)
