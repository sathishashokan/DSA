# BRUTE FORCE
# def rotate_90(matrix):
#     n = len(matrix)
#     # Create a new matrix of same size to store rotated result
#     rotated = [[0] * n for _ in range(n)]
#
#     # Traverse each element of original matrix
#     for i in range(n):
#         for j in range(n):
#             # Place the element at its new rotated position
#             rotated[j][n - i - 1] = matrix[i][j]
#
#     # Return the rotated matrix
#     return rotated

def rotate_90(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()


arr = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] # n = 6
arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # n = 10
arr2 = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
print(rotate_90(arr2))
for row in range(len(arr2)):
    print(arr2[row])
