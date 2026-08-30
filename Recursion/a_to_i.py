# string to int
INT_MAX = 2**31-1
INT_MIN = -2**31

def helper(s, i, total, sign):
    if i >= len(s) or not s[i].isdigit():
        return sign * total
    total = total*10 + int(s[i])

    if total * sign >= INT_MAX: return INT_MAX
    if total * sign <= INT_MIN: return INT_MIN

    return helper(s, i+1, total, sign)

def string_to_int(s):
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1

    sign = 1
    if i < len(s) and (s[i] == "+" or s[i] == "-"):
        sign = -1 if s[i] == "-" else 1
        i += 1
    return helper(s, i, 0, sign)



s = "42"
s1 = "1337c0d3"
s2 = "0-1"
s3 = "words and 987"
print(string_to_int(s3))