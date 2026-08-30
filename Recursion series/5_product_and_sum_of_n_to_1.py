def product_of_n_to_1(n):
    if n == 1:
        return 1
    return n * product_of_n_to_1(n-1)

def sum_of_n_to_1(n):
    if n == 1:
        return 1
    return n + product_of_n_to_1(n-1)



print(product_of_n_to_1(4))
print(sum_of_n_to_1(4))