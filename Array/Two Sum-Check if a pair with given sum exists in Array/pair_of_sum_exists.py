def pair_exists(arr, target):
    # better approach
    # seen = {}
    # for i, num in enumerate(nums):
    #     diff = target - num
    #     if diff in seen:
    #         return seen[diff], i
    #     seen[num] = i


    # Optimal 1:
    # Membership testing on a set is a hash table lookup. Constant time. You pay O(n) once to build it, then every check inside the loop is basically free.
    # s = set(arr) # O(n), built ONCE
    # n = len(arr)
    # for i in range(n):
    #     missing_element = target-arr[i]
    #     if missing_element in s and arr.index(missing_element) != i: # in s --> O(1) average — hash lookup
    #         return i, arr.index(missing_element)

    # optimal 2:

    # Initialize two pointers: left at start, right at end
    left = 0
    right = len(arr) - 1
    # Create list of tuples (value, original_index)
    element_with_index = [(num, i) for i, num in enumerate(arr)]

    # Sort list based on the values (to apply two-pointer technique)
    element_with_index.sort(key=lambda x: x[0])

    while left < right:
        # Calculate sum of values at pointers
        current_sum = element_with_index[left][0] + element_with_index[right][0]

        if current_sum == target:
            # return "YES"
            return element_with_index[left][1], element_with_index[right][1]
        elif current_sum < target:
            # Sum too small, move left pointer to right to increase sum
            left += 1
        else:
            # Sum too large, move right pointer to left to decrease sum
            right -= 1
    # return "NO"
    return -1, -1



arr = [2,6,5,8,9,11]
arr1 = [2,7,11,15]
arr2 = [3,3]
print(pair_exists(arr1, 13))
