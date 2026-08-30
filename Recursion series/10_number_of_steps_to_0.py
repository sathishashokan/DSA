def helper(n, c):
    if n == 0:
        return c

    if n % 2 == 0:
        return helper(n // 2, c + 1)
    return helper(n - 1, c + 1)


def number_of_steps(num: int) -> int:
    return helper(num, 0)

n = 14
print(number_of_steps(n))
