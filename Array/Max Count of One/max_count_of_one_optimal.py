def max_count_of_one(nums):
    n = len(nums)
    count = 0
    max_count = 0
    for i in range(n):
        if nums[i] == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    # for i in range(n):
    #     if arr[i] == 0:
    #         new_count = i - j
    #         j = i+1
    #         if count < new_count:
    #             count = new_count
    #     elif i == n - 1:
    #         new_count = i - j + 1
    #         if count < new_count:
    #             count = new_count
    return max_count


arr = [1, 1, 0, 1, 1, 1]
arr1 = [1, 0, 1, 1, 0, 1]
arr2 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1,0,1, 1, 1, 1, 1, 1]
print(max_count_of_one(arr2))