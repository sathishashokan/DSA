# BINARY SEARCH
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
        return 0
    last = last_occur(nums, target)
    return last - first + 1

# Driver code
a = [3, 4, 4, 7, 8, 10]
b = [5,7,7,8,8,10,10]
print(occurrence_of_element(a, 3))
