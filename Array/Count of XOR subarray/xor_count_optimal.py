# BRUTE FORCE

# def xor_count(nums, k):
#     n = len(nums)
#     count = 0
#     for i in range(n):
#         xor = 0
#         for j in range(i, n):
#             xor ^= nums[j]
#             if xor == k:
#                 count += 1
#     return count

def xor_count(nums, k):
    count = 0
    freq = {0:1}
    prefix_xor = 0
    for num in nums:
        prefix_xor ^= num
        x = prefix_xor^k
        if x in freq:
            count += freq[x]
        freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
    return count




arr = [4, 2, 2, 6, 4]
arr1 = [5, 6, 7, 8, 9]
print(xor_count(arr, 6))
