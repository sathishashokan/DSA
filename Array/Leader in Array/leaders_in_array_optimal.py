def leaders_in_array(nums):
    # n = len(nums)
    # result = []
    # max_value = float('-inf')
    # # find max, because starting from max sometimes reduce the outer loop iteration
    # max_index = -1
    # for i in range(n):
    #     if nums[i] > max_value:
    #         max_value = nums[i]
    #         max_index = i
    # for i in range(max_index, n):
    #     count = 0
    #     for j in range(i+1, n):
    #         if nums[i] <= nums[j]:
    #             count += 1
    #             break
    #     if count == 0:
    #         result.append(nums[i])
    # return result
    n = len(nums)
    max = nums[-1]
    result = [max]
    for i in range(n-2, -1, -1):
        if nums[i] > max:
            max = nums[i]
            result.append(max)
    result.reverse()
    return result

arr = [4, 7, 1, 0]
arr1 = [10, 22, 12, 3, 0, 6]
arr2 = [1,1,1,1,7]
print(leaders_in_array(arr1))
