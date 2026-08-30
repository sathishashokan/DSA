# BRUTE FORCE
# def rearrangeArray(nums):
#     n = len(nums)
#     pos = []
#     neg = []
#     for i in range(n):
#         if nums[i] > 0:
#             pos.append(nums[i])
#         else:
#             neg.append(nums[i])
#     for i in range(n//2):
#         nums[2*i] = pos[i]
#         nums[2*i+1] = neg[i]
#     return nums

def rearrangeArray(nums):
    n = len(nums)
    temp = [0] * n
    print(temp)
    index_even = 0
    index_odd = 1
    for i in range(n):
        if nums[i] > 0:
            temp[index_even] = nums[i]
            index_even += 2
        else:
            temp[index_odd] = nums[i]
            index_odd += 2
    return temp

arr = [3,1,-2,-5,2,-4]
arr1 = [7,2,4,1,1]
arr2 = [7,1,5,3,6,4]
print(rearrangeArray(arr))
