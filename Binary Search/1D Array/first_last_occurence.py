# Using lower and upper bound
# def lower_bound(nums, target):
#     low = 0
#     high = len(nums) - 1
#     ans = len(nums)
#     while low <= high:
#         mid = (low+high)//2
#         if nums[mid] >= target:
#             ans  = mid
#             high = mid -1
#         else:
#             low = mid + 1
#     return ans
#
# def upper_bound(nums, target):
#     low = 0
#     high = len(nums) - 1
#     ans = len(nums)
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] > target:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans
#
# def occurrence_of_element(nums, target):
#     first = lower_bound(nums, target)
#     if first == len(nums) or first != target:
#         return [-1,-1]
#     last = upper_bound(nums, target)
#     return [first, last-1]


# Using BINARY SEARCH(without lower and upper bound)
def first_occur(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ans = -1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] >= target:
            if nums[mid] == target:
                ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def last_occur(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            if nums[mid] == target:
                ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def occurrence_of_element(nums, target):
    first = first_occur(nums, target)
    if first == -1:
        return [-1, -1]
    last = last_occur(nums, target)
    return [first, last]

# Driver code
a = [3, 4, 4, 7, 8, 10]
b = [5,7,7,8,8,10,10]
print(occurrence_of_element(a, 4))

