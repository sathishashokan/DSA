# OPTIMAL

def spiral_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    top = 0
    right = n - 1 # 3
    bottom = m - 1 # 3
    left = 0
    result = []

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1 # 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1 # 2
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1 # 2
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1 # 1
    return result

arr = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_matrix(arr))