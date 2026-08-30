def longest_sub_of_sum_k(arr, target):
    n = len(arr)
    maxLength = 0

    # starting index
    for startIndex in range(n):
        # ending index
        for endIndex in range(startIndex, n):
            # add all the elements of
            # subarray = arr[startIndex...endIndex]
            currentSum = 0
            for i in range(startIndex, endIndex + 1):
                currentSum += arr[i]
            if currentSum == target:
                maxLength = max(maxLength, endIndex - startIndex + 1)
    return maxLength


arr = [10, 5, 2, 7, 1, 9]
arr1 = [-3, 2, 1]
arr2 = [4,1,1,2]
arr3 = [9, -3, 3, -1, 6, -5]
print(longest_sub_of_sum_k(arr2, 4))