# Find the Peak element and return its index using BINARY SEARCH
def find_peak(nums):
    n = len(nums)
    if n == 1:
        return 0
    low = 1
    high = n - 2
    if float('-inf') < nums[0] > nums[1]:
        return 0
    if nums[n-2] < nums[n-1] > float('-inf'):
        return n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid-1] < nums[mid] > nums[mid+1]:
            return mid
        if nums[mid-1] < nums[mid] < nums[mid+1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def occurrence_of_element(nums):
    index = find_peak(nums)
    return index

# Driver code
a = [1,2,3,1]
b = [1,2,1,3,5,6,4]
c = [1,2,3,4,5,6,7,8,5,1]
print(occurrence_of_element(a))
