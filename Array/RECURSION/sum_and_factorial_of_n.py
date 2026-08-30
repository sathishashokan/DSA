def sum_of_n(n):
    if n == 0:
        return 0
    return n + sum_of_n(n-1)

# using parametrized method
def sum_of_n_para(i, sum):
    if i == 0:
        print(sum)
        return
    sum_of_n_para(i-1, sum+i)

def factorial_of_n(n):
    if n == 0:
        return 1
    return n * factorial_of_n(n-1)

# print(sum_of_n(4))

# print(factorial_of_n(3))

print(sum_of_n_para(4,0))