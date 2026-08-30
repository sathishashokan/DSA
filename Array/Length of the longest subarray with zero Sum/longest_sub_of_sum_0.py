def longest_sub_of_sum_0(arr):
    # Brute Force Approach

    n = len(arr)
    result = 0
    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for k in range(i, j+1):
                current_sum += arr[k]
            if current_sum == 0:
                result = max(result, j - i + 1)
    return result

arr = [6, -2, 2, -8, 1, 7, 4, -10]
arr1 = [-3, 2, 1]
arr2 = [4,1,1,2]
arr3 = [-3, 3, -1, 6, -5, 9]
print(longest_sub_of_sum_0(arr3))