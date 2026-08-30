# My Recursion approach

# class Solution:
#     def my_pow(self, x, n):
#         if n == 0:
#             return 1
#         temp = n
#         if temp < 0:
#             temp = temp * -1
#
#         product = self.my_pow(x,temp-1)
#         if n < 0:
#             return 1/(product*x)
#         return product * x

# Iterative Approach

# def myPow(x, n):
#     ans = 1.00000
#     m = n
#     if n < 0:
#         n = n * -1
#     while n > 0:
#         if n%2 == 0:
#             x = x * x
#             n = n//2
#         else:
#             ans *= x
#             n = n - 1
#     if m < 0:
#         return 1/ans
#     return ans

# Recursion Approach

def power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n%2==0:
        return power(x*x, n//2)
    return x * power(x, n-1)


def myPow(x, n):
    if n < 0:
        return 1.0/power(x, -n)
    return power(x, n)




print(myPow(2.00000,-2))