# Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
# Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0

def move_zeros(nums):
    j = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break
    if j == -1:
        return nums
    for i in range(j+1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

arr = [0]
arr1 = [2,2,2,5,3,3,3,6,3,4,4]
arr2 = [1, 0, 2, 3,2,0,0,4,5,1]
print(move_zeros(arr2))