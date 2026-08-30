def reverse_triangle_pattern(r, c):
    if r == 0:
        return
    if c < r:
        print("*",end=" ")
        reverse_triangle_pattern(r, c+1)
    else:
        print()
        reverse_triangle_pattern(r-1, 0)


def triangle_pattern(r, c):
    if r == 0:
        return
    if c < r:
        triangle_pattern(r, c + 1)
        print("*", end=" ")
    else:
        triangle_pattern(r - 1, 0)
        print()


n = 5
reverse_triangle_pattern(n, 0)
triangle_pattern(n, 0)