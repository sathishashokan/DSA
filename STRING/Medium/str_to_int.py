INT_MIN = -2**31
INT_MAX = 2**31 - 1

def helper(s, i, total, sign):
    # Base condition
    if i >= len(s) or not s[i].isdigit():
        return sign * total

    total = (total * 10) + int(s[i])

    if sign * total >= INT_MAX: return INT_MAX
    if sign * total <= INT_MIN: return INT_MIN

    return helper(s, i+1, total, sign)


def Atoi(s):
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    sign = 1
    if i < len(s) and (s[i] == '-' or s[i] == '+'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    return helper(s, i, 0, sign)

s1 = "42"
s2 = " -042"
s3 = "1337c0d3"
s4 = "0-1"
s5 = "words and 987"
s6 = "  2147483649s"
print(Atoi(s6))
