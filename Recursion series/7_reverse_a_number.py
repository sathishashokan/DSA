# Approach 1

# def reverse_a_number(num):
#     if num == 0:
#         return 0
#
#     rem = num%10
#     digit = len(str(num))
#     return (rem*(10**(digit-1))) + reverse_a_number(num//10)

# Approach 2
rev_num = 0

def reverse_a_number(num):
    global rev_num
    if num == 0:
        return

    rem = num%10
    rev_num = (rev_num * 10) + rem
    reverse_a_number(num//10)


num = 5721
print(reverse_a_number(num))
print(rev_num)
