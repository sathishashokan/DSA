# BINARY SEARCH

def calculate_days(nums, weight_per_day, days):
    weight = 0
    calc_days = 0
    for num in nums:
        weight += num
        if weight > weight_per_day:
            weight = num
            calc_days += 1
    if weight <= weight_per_day:
        calc_days += 1
    return calc_days <= days

def min_ship_capacity(nums, days):
    low = max(nums)
    high = sum(nums)
    while low <= high:
        mid = (low+high)//2
        if calculate_days(nums, mid, days):
            high = mid - 1
        else:
            low = mid + 1
    return low

# Driver code
a = [5, 4, 5, 2, 3, 4, 5, 6]
b = [1,2,3,4,5,6,7,8,9,10]
c = [1,2,3,4,5]
d = [3,2,2,4,1,4]
e = [1,2,3,1,1]
print(min_ship_capacity(b,1))
