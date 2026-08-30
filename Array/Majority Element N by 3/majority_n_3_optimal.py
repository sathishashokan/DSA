# BRUTE FORCE

# def majority_element_n_3(nums):
#     n = len(nums)
#     hash = {}
#     result = []
#     for num in nums:
#         hash[num] = hash.get(num, 0) + 1
#         if hash[num] == (n//3 + 1):
#             result.append(num)
#         if len(result) == 2:
#             break
#     return result

def majority_n_3(nums):
    n = len(nums)
    count1, count2 = 0, 0
    el1 = float('-inf')
    el2 = float('-inf')
    result = []

    for num in nums:
        if count1 == 0 and num != el2:
            count1 = 1
            el1 = num
        elif count2 == 0 and num != el1:
            count2 = 1
            el2 = num
        elif el1 == num:
            count1 += 1
        elif el2 == num:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    if nums.count(el1) >= n//3 + 1:
        result.append(el1)
    if nums.count(el2) >= n // 3 + 1:
        result.append(el2)
    return result


arr = [1, 2, 1, 1, 1, 2]
arr1 = [1, 2, 1, 1, 3, 2, 2]
arr2 = [1,1,1,3,3,2,2,2]
print(majority_n_3(arr2))
