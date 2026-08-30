def n_to_one(n):
    if n == 0:
        return

    print(n)
    n_to_one(n-1)

def one_to_n(n):
    if n == 0:
        return

    one_to_n(n-1)
    print(n)

def print_both(n):
    if n == 0:
        return

    print(n)
    print_both(n-1)
    print(n)

# one_to_n(5)
# n_to_one(5)
print_both(5)