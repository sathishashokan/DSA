def longest_sub_of_sum_k(arr, target):
    n = len(arr)
    start = 0
    max_sub = 0
    end  = 0
    sub_count = arr[start]

    while end < n:
        while start <= end and sub_count > target:
            sub_count -= arr[start]
            start += 1

        if sub_count == target:
            max_sub = max(max_sub, (end - start) + 1)

        end += 1
        if end < n:
            sub_count += arr[end]
    return max_sub


arr = [10, 5, 2, 7, 1, 9]
arr1 = [-3, 2, 1]
arr2 = [4,1,1,2]
print(longest_sub_of_sum_k(arr2,4))
