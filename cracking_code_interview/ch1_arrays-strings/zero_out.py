def zero_out(matrix):

	# tracker lists to keep the columns and rows to zero out
	columns_to_zero = [False] * len(matrix[0])
	rows_to_zero = [False] * len(matrix)

	for outer_idx, row in enumerate(matrix):
		for inner_idx, cell in enumerate(row):
			# if we find a zero. set the appropriate indicies in trackers to True
			if cell == 0:
				columns_to_zero[inner_idx] = True
				rows_to_zero[outer_idx] = True
	
	# go through our columns to zero out

	for idx, val in enumerate(columns_to_zero):
		# if true, we zero all columns/cells in each row of matrix 
		if val:
			for row in matrix:
				row[idx] = 0
	
	# go trough rows and zero out
	for idx, val in enumerate(rows_to_zero):
		if val:
			matrix[idx] = [0] * len(matrix[idx])


	return matrix

my_matrix = [[1,1,1,0], [0, 1, 1, 1], [1, 1, 1, 1]]

assert zero_out(my_matrix) == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0]]
