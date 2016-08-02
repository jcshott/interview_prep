# a b c
# d e f
# g h i
#
# given a matrix, print items in spiral form
# abcfihgde
#
# [[a, b, c], [d, e, f]..]

def print_spiral(matrix):

    last_start_row = 0
    last_start_col = len(matrix) - 1
    curr_row = 0
    curr_col = 0

    while curr_col < len(matrix[0]):
        print matrix[curr_row][curr_col]
        curr_col += 1
    curr_row += 1
    while curr_row < len(matrix):
        print matrix[curr_row][curr_col]
        curr_row += 1
    curr_col -= 1
    while curr_col >= 0:
        print matrix[curr_row][curr_col]
        curr_col -= 1
    curr_col += 1
    curr_row -= 1
    while curr_row > last_start_row:
        print matrix[curr_row][curr_col]
        curr_row -= 1


print_spiral([[1,2,3], [4,5,6], [7,8,9]])
