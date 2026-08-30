# BRUTE FORCE

# def sum4(nums, target):
#     res = []
#     n =len(nums)
#     for a in range(n):
#         for b in range(a+1, n):
#             for c in range(b+1, n):
#                 for d in range(c+1, n):
#                     if nums[a] + nums[b] + nums[c] + nums[d] == target:
#                         sub = [nums[a], nums[b], nums[c], nums[d]]
#                         sub.sort()
#                         if sub not in res:
#                             res.append(sub)
#     return res

# BETTER APPROACH
# def sum4(nums, target):
#     n = len(nums)
#     res = set()
#     for i in range(n):
#         for j in range(i+1, n):
#             hash_set = set()
#             for k in range(j + 1, n):
#                 req = target - nums[i] - nums[j] - nums[k]
#                 if req in hash_set:
#                     quads = tuple(sorted([nums[i],nums[j],nums[k],req]))
#                     res.add(quads)
#                 hash_set.add(nums[k])
#
#     return [list(quads) for quads in res]

def sum4(nums, target):
    n = len(nums)
    nums.sort()
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                quads = nums[i] + nums[j] + nums[left] + nums[right]
                if quads == target:
                    res.append([nums[i],nums[j],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif quads < target:
                    left += 1
                else:
                    right -= 1
    return res


arr = [1,0,-1,0,-2,2]
arr1 = [2,2,2,2,2]
arr2 = [1,1,1,3,3,2,2,2]
print(sum4(arr1, 8))
