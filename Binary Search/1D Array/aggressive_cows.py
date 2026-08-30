# OPTIMAL(BINARY SEARCH)
def can_be_placed(nums, gap, cows):
    nums.sort()
    cow_count = 1
    last_pos = nums[0]
    for i in range(1, len(nums)):
        if (nums[i] - last_pos) >= gap:
            cow_count += 1
            last_pos = nums[i]
    return cow_count >= cows

def aggressive_cows(nums, k):
    l, h = 1, (max(nums) - min(nums))
    while l <= h:
        m = (l+h)//2
        if can_be_placed(nums, m, k):
            l = m + 1
        else:
            h = m - 1
    return h

# Driver code
a = [0,3,4,7,10,9]
b = [4,2,1,3,6]
print(aggressive_cows(b,2))
