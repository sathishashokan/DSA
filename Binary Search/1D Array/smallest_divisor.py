# BINARY SEARCH
from math import ceil

def sum_of_divisor(nums, divisor, limit):
    sum = 0
    for num in nums:
        sum += ceil(num/divisor)
    return sum <= limit

def smallest_divisor(nums, limit):
    low = 1
    high = max(nums)
    while low <= high:
        mid = (low+high)//2
        if sum_of_divisor(nums, mid, limit):
            high = mid - 1
        else:
            low = mid + 1
    return low


# Driver code
a = [1,2,5,9]
b = [44,22,33,11,1]
c = [1,2,3,4,5]
d = [8,4,2,3]
print(smallest_divisor(d,10))
