def reverse_a_number(num):
    if num == 0:
        return 0

    rem = num%10
    digit = len(str(num))
    return (rem*(10**(digit-1))) + reverse_a_number(num//10)

def palindrome(num):
    return num == reverse_a_number(num)


num = 12321
print(palindrome(num))
