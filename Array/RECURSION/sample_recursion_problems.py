def print_n_times(n):
    if n < 1:
        return
    print("HI")
    print_n_times(n-1)

def print_1_to_n(i, n):
    if i > n:
        return
    print(i)
    print_1_to_n(i+1, n)

def print_n_to_1(n):
    if n < 1:
        return
    print(n)
    print_n_to_1(n-1)

def print_1_to_n_using_back_tracking(i):
    if i < 1:
        return
    print_1_to_n_using_back_tracking(i-1)
    print(i)

def print_n_to_1_using_back_tracking(i, n):
    if i > n:
        return
    print_n_to_1_using_back_tracking(i+1, n)
    print(i)

num = 5
# print_n_times(n)

# print_1_to_n(1, 5)

# print_n_to_1(5)

# print_1_to_n_using_back_tracking(3)

print_n_to_1_using_back_tracking(1, 3)