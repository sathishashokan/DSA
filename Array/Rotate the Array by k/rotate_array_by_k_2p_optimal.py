# Brute Force

# def rotate_right_by_k(arr, k):
#     n = len(arr)
#     temp = arr[-k:]
#     for i in range(n-k, 0, -1):
#         arr[i+1] = arr[i-1]
#     for i in range(k):
#         arr[i] = temp[i]
#     print(arr)

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate(nums, k):
    n = len(nums)
    if n == 0 or k == 0:
        return nums
    k %= n

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

arr = [1,1,2,2,2,3,3]
arr1 = [1,2,3,4,5,6,7]
arr2 = [-10,100,8,12]
print(rotate(arr1, 2))
