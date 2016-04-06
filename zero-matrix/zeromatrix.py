"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]

Make sure it works with more than one zero found:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12]])
    [[0, 0, 0, 0], [5, 0, 0, 8], [0, 0, 0, 0]]

"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""
    # keep track of all the row nums and cell/col nums that will need to be zeroed out
    rows_to_zero = set()
    cols_to_zero = set()

    # we can't change the row/column right away because that will essentially make everything zero.
    # so grab the places where we have a zero and add indexes to list
    for outer_idx, row in enumerate(matrix):
        for inner_idx, cell in enumerate(row):
            if cell == 0:
                rows_to_zero.add(outer_idx)
                cols_to_zero.add(inner_idx)

    # # for each row we found that has a zero, set that row to all zeros
    for row_num in rows_to_zero:
        matrix[row_num] = len(matrix[row_num]) * [0]
   

    # # for each row in our matrix, set all the columns/cells found in our cols_to_zero list to zero
    
    for col_num in cols_to_zero:
        for idx in xrange(len(matrix)):
            matrix[idx][col_num] = 0

    return matrix

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TESTS PASSED! YOU'RE DOING GREAT!\n"
