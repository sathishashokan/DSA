# BRUTE FORCE

# def missing_number(nums, k):
#     for num in nums:
#         if num <= k:
#             k += 1
#         else:
#             break
#     return k

# OPTIMAL(BINARY SEARCH)
def missing_number(nums, k):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low+high)//2
        missing = nums[mid] - (mid+1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return low + k

# Driver code
a = [2,3,4,7,11]
b = [1,2,3,4]
c = [1,2,3,4,5]
print(missing_number(a,5))
