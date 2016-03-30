def merge_sort(lst):
	"""sort an unsorted list using merge sort. takes in list, returns that list, sorted
	>>> nums = [4, 3, 5, 7, 9, 10, 1, 2]
	>>> merge_sort(nums)
	>>> nums
	[1, 2, 3, 4, 5, 7, 9, 10]
	"""

	if len(lst) > 1:
		mid = len(lst)/2
		left = lst[:mid]
		right = lst[mid:]
		
		merge_sort(left)
		merge_sort(right)

		i = 0
		j = 0
		k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				lst[k] = left[i]
				i += 1
			else:
				lst[k] = right[j]
				j += 1
			k+=1
		
		while i < len(left):
			lst[k]=left[i]
			i+=1
			k+=1
		
		while j < len(right):
			lst[k]=right[j]
			j+=1
			k+=1


if __name__=='__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n*** ALL TESTS PASSED. Good Job!\n"

	
