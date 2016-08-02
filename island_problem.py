"""
Find the number of islands | Set 1 (Using DFS)
Given a boolean 2D matrix, find the number of islands.

What is an island?
A group of connected 1s forms an island. For example, the below matrix contains 5 islands

{1, 1, 0, 0, 0},
{0, 1, 0, 0, 1},
{1, 0, 0, 1, 1},
{0, 0, 0, 0, 0},
{1, 0, 1, 0, 1}
"""

def count_islands(matrix):
    if len(matrix) < 1:
        return 0

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    seen = [[False for x in range(num_cols)] for y in range(num_rows)]
    num_islands = 0

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 1 and not seen[i][j]:
                # find connected 1s
                dfs(matrix, seen, i, j, num_rows, num_cols)
                num_islands += 1
    return num_islands


def dfs(matrix, visited, i, j, rows, cols):
    if i < 0 or j < 0:
        return
    if i > rows-1 or j > cols-1:
        return
    if matrix[i][j] == 0 or visited[i][j]:
        return
    visited[i][j] = True

    dfs(matrix, visited, i+1, j, rows, cols)
    dfs(matrix, visited, i, j+1, rows, cols)
    dfs(matrix, visited, i+1, j+1, rows, cols)
    dfs(matrix, visited, i-1, j, rows, cols)
    dfs(matrix, visited, i-1, j-1, rows, cols)
    dfs(matrix, visited, i, j-1, rows, cols)
    dfs(matrix, visited, i+1, j-1, rows, cols)
    dfs(matrix, visited, i-1, j+1, rows, cols)


islands = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]

islands2 = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1]]
print count_islands(islands)
