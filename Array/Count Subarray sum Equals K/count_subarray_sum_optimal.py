# BRUTE FORCE
# Loop through all the available subarray and count if sum equals to k. Finally return k


# OPTIMAL

def count_subarray(arr, k):
    n = len(arr)
    prefix_hash = {0: 1}
    prefix_sum = 0
    count = 0

    for i in range(n):
        prefix_sum += arr[i]
        prefix = prefix_sum - k
        if prefix in prefix_hash:
            count += prefix_hash[prefix]
        prefix_hash[prefix_sum] = prefix_hash.get(prefix_sum, 0) + 1

    return count


arr = [3, 1, 2, 4]
arr1 = [1,2,3]
arr2 = [1,2,3,-3,1,1,1,4,2,-3]
print(count_subarray(arr2, 3))