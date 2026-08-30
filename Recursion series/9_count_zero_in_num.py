def count_zero(num, count):
    if num == 0:
        return count
    if num%10 == 0:
        count += 1
    return count_zero(num//10, count)


num = 30204
print(count_zero(num, 0))
