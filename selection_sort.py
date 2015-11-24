def find_smallest_index(array, start_idx):
	""" takes an array and a number start_idx
		returns the index of the smallest value that occurs with index start_idx or greater.
	"""
	min_val = array[start_idx]
	min_idx = start_idx

	for x in range(min_idx+1, len(array)):
		if array[x] <= min_val:
			min_idx = x
			min_val = array[x]
	return min_idx

def swap(array, first_idx, second_idx):
	""" takes in an array, and two numbers - representing the two numbers to swap
		returns the new array
	"""
	array[first_idx], array[second_idx] = array[second_idx], array[first_idx]
	return array

def selection_sort(array):
	min_idx = 0

	for x in range(len(array)):
		min_idx = find_smallest_index(array, x)
		swap(array, min_idx, x)

	return array

print selection_sort([-3, 5, 3, -3, 1, 0, 22, 10])