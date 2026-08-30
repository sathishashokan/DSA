# OPTIMAL(BINARY SEARCH)
def painting_time(nums, k):
    low = max(nums)
    high = sum(nums)
    while low <= high:
        mid = (low+high)//2
        total = 0
        c_c = 1
        for num in nums:
            if total+num <= mid:
                total += num
            else:
                c_c += 1
                total = num
        if c_c <= k:
            high = mid - 1
        else:
            low = mid + 1
    return low


# Driver code
a = [5, 5, 5, 5]
b = [10, 20, 30, 40]
print(painting_time(b,2))
