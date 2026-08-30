# BRUTE FORCE

# def repeat_and_miss(nums):
#     a = b = 0
#     for i in range(1, len(nums) + 1):
#         count = nums.count(i)
#         if count == 2:
#             a = i
#         elif count == 0:
#             b = i
#         if a != 0 and b != 0:
#             break
#     return [a,b]

def repeat_and_miss(nums):
    n = len(nums)
    sn = (n * (n+1))//2
    s2n = (n * (n+1) * (2*n+1))//6
    s = 0
    s2 = 0
    for num in nums:
        s += num
        s2 += num*num
    val1 = s - sn  # x-y
    val2 = s2 - s2n # x^2 - y^2 -> (x-y)(x+y)
    val2 = val2//val1 # x+y = val2/(x-y)
    x = (val1+val2)//2 # (x+y)+(x-y) = some_value -> x = some_value/2
    y = val2 - x # x+y = val2 -> y = val2 - x (or) x-y = val1 --> -y = val1-x --> y = x - val1
    return [x,y]




arr = [1, 2, 3, 6, 7, 5, 7]
arr1 = [3, 5, 4, 1, 1]
arr2 = [1,2,3,4,5,6,6]
print(repeat_and_miss(arr2))
