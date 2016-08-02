# Enter your code here. Read input from STDIN. Print output to STDOUT

def print_spiral(matrix):

    top = 0
    bottom = len(matrix)-1
    left = 0
    right = len(matrix[0]) -1
    output = []
    while True:
        #print "left", left
        #print "right", right
        #print "top", top
        #print "bottom", bottom
        # print top row
        for x in matrix[top][left:right+1]:
            output.append(x)
        top += 1
        if top > bottom or left > right:
            break
        #print right col
        for r in range(top, len(matrix)):
            output.append(matrix[r][right])
        right -= 1
        if top > bottom or left > right:
            break
        # print bottom
        for b in range(len(matrix[0])-(left+right)-1,left-1, -1):
            #print "b", b
            output.append(matrix[bottom][b])
        bottom -= 1
        if top > bottom or left > right:
            break
        #print left col
        for l in range(len(matrix)-(bottom+top), top-1, -1):
            output.append(matrix[l][left])
        left += 1

        if top > bottom or left > right:
            break
    print ",".join(output)

# build matrix
matrix_size = raw_input().split(",")
_matrix = []
for x in range(int(matrix_size[0])):
    row = raw_input().split(",")
    _matrix.append(row)

print_spiral(_matrix)
