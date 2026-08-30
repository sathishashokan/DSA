# BINARY SEARCH

#ITERATION APPROACH
# def binary_search(nums, target):
#     low = 0
#     high = len(nums) - 1
#     while low <= high:
#         mid = (low+high)//2
#         if nums[mid] == target:
#             return mid
#         elif target > nums[mid]:
#             low = mid + 1
#         else:
#             high = mid -1
#     return -1

# RECURSION APPROACH
def is_target(nums, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return is_target(nums, mid + 1, high, target)
    else:
        return is_target(nums, low, mid - 1, target)

def binary_search(nums, target):
    return is_target(nums, 0, len(nums) - 1, target)



# Driver code
# a = [1,2,-3,0,-4,-5]
b = [-1,0,3,5,9,12]
# c = [2,3,-2,4]
# d = [-2,0,-1]
# e  = [-1,-2,-10]
print(binary_search(b, 12))
# print(a)
  