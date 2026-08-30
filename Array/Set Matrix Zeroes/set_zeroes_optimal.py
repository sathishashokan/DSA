# BRUTE FORCE

# def set_matrix_zero(matrix):
#     m = len(matrix)
#     # Get number of columns
#     n = len(matrix[0])
#
#     # First pass: mark rows and columns
#     for i in range(m):
#         for j in range(n):
#             # If current cell is zero
#             if matrix[i][j] == 0:
#                 # Mark entire row
#                 for col in range(n):
#                     if matrix[i][col] != 0:
#                         matrix[i][col] = -1
#                 # Mark entire column
#                 for row in range(m):
#                     if matrix[row][j] != 0:
#                         matrix[row][j] = -1
#     for i in range(m):
#         print(matrix[i])
#
#     # Second pass: replace -1 with 0
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] == -1:
#                 matrix[i][j] = 0
def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    is_first_column_0 = False
    is_first_row_0 = False

    # Check if first row has any zero
    for j in range(n):
        if matrix[0][j] == 0:
            is_first_row_0 = True
            break

    # Check if first column has any zero
    for i in range(m):
        if matrix[i][0] == 0:
            is_first_column_0 = True
            break

    for i  in range(1,m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    print(matrix)

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # if necessary replace 1st row with zero
    if  is_first_row_0:
        for j in range(n):
            matrix[0][j] = 0

    # if necessary replace 1st column with zero
    if is_first_column_0:
        for i in range(m):
            matrix[i][0] = 0



arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] # n = 6
arr1 = [[1,1,1],[1,0,1],[1,1,1]] # n = 10
arr2 = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
setZeroes(arr1)
for row in range(len(arr1)):
    print(arr1[row])
