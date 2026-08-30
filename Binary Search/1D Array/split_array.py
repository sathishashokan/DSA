# OPTIMAL(BINARY SEARCH)
def split_array(nums, k):
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
a = [1,2,3,4,5]
b = [3,5,1]
c = [7,2,5,10,8]
print(split_array(c,2))
