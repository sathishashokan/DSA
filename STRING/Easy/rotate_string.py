#My Approach

# def rotate(s,t):
#     for i in range(1, len(s)):
#         temp = s[i:]+s[:i]
#         if temp == t:
#             return True
#     return False

# Leet code Approach
def rotate(s,t):
    if len(s) != len(t):
        return False
    double_s = s+s
    return t in double_s


s1 = "abcde"
s2 = "abcede"
print(rotate(s1,s2))