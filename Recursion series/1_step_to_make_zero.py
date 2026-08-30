def helper(n, c):
    if n == 0:
        return c

    if n%2==0: # if number is even divide by 2
        return helper(n//2, c + 1)
    return helper(n-1, c + 1) # if number is odd subtract 1

def steps_to_make_zero(n):
    return helper(n, 0)

n = 14
print(steps_to_make_zero(n))