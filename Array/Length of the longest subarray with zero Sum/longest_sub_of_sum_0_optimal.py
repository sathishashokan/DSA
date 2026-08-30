def longest_sub_of_sum_0(arr):
    # optimal Approach using Hash Map(Dict)

    seen = {}
    sum = 0
    max_length = 0

    for i, num in enumerate(arr):
        sum += num

        if sum == 0:
            max_length = i + 1
        elif sum in seen:
            max_length = max(max_length, i - seen[sum])
        else:
            seen[num] = i
    return  max_length


arr = [6, -2, 2, -8, 1, 7, 4, -10]
arr1 = [-3, 2, 1]
arr2 = [9,-3,3,-1,6,-5]
arr3 = [-3, 3, -1, 6, -5, 9]
print(longest_sub_of_sum_0(arr2))