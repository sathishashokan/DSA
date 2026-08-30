# BRUTE FORCE

def merge_two_arrays(nums1, nums2, m, n):
    j = 0
    for i in range(m, m+n):
        nums1[i] = nums2[j]
        j += 1
    nums1.sort()
    # if n == 0:
    #     return
    # j = 0
    # while j < n:
    #     nums1[m+j] = nums2[j] # m will be length of nums1 without zeros
    #     j += 1
    # print(nums1)
    # is_true = True
    # while is_true:
    #     i = 1
    #     count = 0
    #     while i < m+n:
    #         if nums1[i-1] > nums1[i]:
    #             nums1[i-1], nums1[i] = nums1[i], nums1[i-1]
    #             count = 1
    #         i += 1
    #     if count == 0:
    #         is_true = False

arr = [-5, -2, 4, 5, 0, 0, 0]
arr1 = [-3, 1, 8]
merge_two_arrays(arr,arr1,4,3)
print(arr)
