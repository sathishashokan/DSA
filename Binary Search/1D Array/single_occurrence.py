# BINARY SEARCH
def find_single_occur(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    low = 1
    high = n - 2

    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]
    while low <= high:
        mid = (low+high)//2
        if nums[mid-1] != nums[mid] != nums[mid+1]:
            return nums[mid]
        if (mid%2==1 and nums[mid-1] == nums[mid]) or \
            (mid%2==0 and nums[mid] == nums[mid+1]):
            low = mid + 1
        else:
            high = mid - 1
    return -1


def occurrence_of_element(nums):
    index = find_single_occur(nums)
    return index

# Driver code
a = [1,1,2,2,3,3,4,5,5,6,6]
b = [1,1,2,2,3,4,4]
c = [0,0,1,1,2,2,3,4,4,5,5]
print(occurrence_of_element(c))
