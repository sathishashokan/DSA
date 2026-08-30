# BINARY SEARCH
def find_small(nums):
    low = 0
    high = len(nums) - 1
    min_value = float('inf')
    while low <= high:
        mid = (low+high)//2
        if nums[low] <= nums[high]: #if this is true, then this means that the entire part is sorted
            min_value = min(min_value, nums[low])
            break
        if nums[low] <= nums[mid]:
            min_value = min(min_value,nums[low])
            low = mid + 1
        else:
            min_value = min(min_value,nums[mid])
            high = mid - 1
    return min_value

def occurrence_of_element(nums):
    index = find_small(nums)
    return index

# Driver code
a = [3,1,2,3,3,3,3]
b = [5,6,7,8,1,2,3,4]
c = [5,0,1,2,3]
print(occurrence_of_element(c))