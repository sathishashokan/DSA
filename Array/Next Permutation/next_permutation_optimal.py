# BRUTE FORCE
# from itertools import permutations
# def permutation(nums):
#     perms = sorted(set(permutations(nums)))
#     current = tuple(nums)
#     for i in range(len(perms)):
#         if perms[i] == current:
#             if i == len(perms)-1:
#                 return list(perms[0])
#             return list(perms[i+1])



def permutation(nums):
    n = len(nums)
    index = -1
    # find the first smaller element from the end - 1
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            index = i
            break
    if index == -1:
        nums.reverse()
        return nums

    for i in range(n-1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

    nums[index+1:] = reversed(nums[index+1:])

    return nums


arr = [3,2,1]
arr1 = [1,3,2]
print(permutation(arr))