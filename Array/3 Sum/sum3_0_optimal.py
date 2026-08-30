# BRUTE FORCE

# def sum3_0(nums):
#     res = []
#     n =len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             for k in range(j+1, n):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     sub = [nums[i], nums[j], nums[k]]
#                     sub.sort()
#                     if sub not in res:
#                         res.append(sub)
#     return res

# BETTER APPROACH
# def sum3_0(nums, n):
#     res = set()
#     for i in range(n):
#         hash_set = set()
#         for j in range(i+1, n):
#             third = -(nums[i] + nums[j])
#             if third in hash_set:
#                 triplet = tuple(sorted([nums[i],nums[j],third]))
#                 res.add(triplet)
#             hash_set.add(nums[j])
#
#     return [list(triplet) for triplet in res]

def sum3_0(nums, n):
    nums.sort()
    res = []
    for i in range(n):
        if nums[i] > 0: #because in a sorted array after 0 everything is positive. So no use of finding triplet with sum 0.
            break
        left = i+1
        right = n-1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while left < right:
            triplet = nums[i] + nums[left] + nums[right]
            if triplet == 0:
                res.append([nums[i],nums[left],nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif triplet < 0:
                left += 1
            else:
                right -= 1
    return res


arr = [-1,0,1,2,-1,-4]
arr1 = [1, 2, 1, 1, 3, 2, 2]
arr2 = [1,1,1,3,3,2,2,2]
print(sum3_0(arr, 6))
