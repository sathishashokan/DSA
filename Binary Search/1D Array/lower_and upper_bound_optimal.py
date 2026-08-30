#search insert position and lower bound have the same solution

#optimal
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    while low <= high:
        mid = (low+high)//2
        # if nums[mid] > target: # This is the only change for upper bound problem
        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

a = [1,2,2,3]
b = [3,5,8,15,19]
print(binary_search(a, 16))