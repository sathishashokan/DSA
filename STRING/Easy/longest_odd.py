# MY APPROACH and Leet code Approach
def longest_odd(s):
    for i in range(len(s)-1, -1, -1):
        if int(s[i])%2 == 1:
            return s[:i+1]
    return ""


s1 = "52"
s2 = "4206"
s3 = "35427"
print(longest_odd(s3))