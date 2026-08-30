# BRUTE FORCE
# Using all the available subarrays

# Optimal
def max_subarray_product(nums):
    pre = 1
    suff = 1
    ans = float('-inf')
    n = len(nums)
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= nums[i]
        suff *= nums[n-i-1]
        ans = max(ans, suff, pre)
    return ans

# Driver code
a = [1,2,-3,0,-4,-5]
b = [1,2,3,4,5,0]
c = [2,3,-2,4]
d = [-2,0,-1]
e  = [-1,-2,-10]
print(max_subarray_product(e))
# print(a)
