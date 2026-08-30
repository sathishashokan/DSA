def sum_of_digit(num, sum):
    if num == 0:
        return sum
    sum = sum + num%10
    return sum_of_digit(num//10, sum)

def product_of_digit(num, product):
    if num == 0:
        return product
    product = product * (num%10)
    return product_of_digit(num//10, product)

num = 1234
print(sum_of_digit(num, 0))
print(product_of_digit(num, 1))