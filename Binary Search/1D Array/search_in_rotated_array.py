def find_index(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        # for array containing duplicate we need below 4 lines
        # if nums[low] == nums[mid] == nums[high]:
        #     low += 1
        #     high -= 1
        #     continue
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def occurrence_of_element(nums, target):
    index = find_index(nums, target)
    return index

# Driver code
a = [3,1,2,3,3,3,3]
b = [5,6,1,2,3,4]
print(occurrence_of_element(a, 3))