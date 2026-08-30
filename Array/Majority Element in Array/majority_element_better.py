def majority_element(nums):
    n = len(nums)
    hash_occur = {}
    for num in nums:
        if num in hash_occur:
            hash_occur[num] += 1
            if hash_occur[num] > n // 2:
                return num
        else:
            hash_occur[num] = 1

    return -1


arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
arr1 = [1, 1, 1, 2, 1, 2]
arr2 = [1,1,2,0]
arr3 = [0,2,0,2]
print(majority_element(arr1))