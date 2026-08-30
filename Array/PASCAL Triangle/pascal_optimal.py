# BRUTE FORCE

# def pascal(r):
#     triangle = []
#
#     # Loop for each row
#     for i in range(r):
#         # Create a row with size (i+1) and initialize all elements to 1
#         row = [1] * (i + 1)
#
#         # Fill elements from index 1 to i-1 (middle values)
#         for j in range(1, i):
#             # Each element = sum of two elements above it
#             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#
#         # Add current row to the triangle
#         triangle.append(row)
#     return triangle


# OPTIMAL

def generate_row(N):
    result = []
    value = 1
    result.append(value)
    for i in range(1, N):
        value = value * (N-i)//i
        result.append(value)
    return result

def pascal(n):
    answer = []
    for i in range(1, n+1):
        answer.append(generate_row(i))
    return answer

print(pascal(6))