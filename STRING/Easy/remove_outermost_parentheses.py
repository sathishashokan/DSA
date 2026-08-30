# MY APPROACH
# def remove_outer_parentheses(s):
#     count = 1
#     starting_index = 0
#     new_str = ""
#     for i in range(1,len(s)):
#         if s[i] == "(":
#             count += 1
#         else:
#             count -= 1
#         if count == 0:
#             end_index = i
#             new_str += s[starting_index + 1:end_index]
#             starting_index = i+1
#     return new_str

# Leet code Approach
def remove_outer_parentheses(s):
    total = 0
    result = ""
    for i in s:
        if i == '(':
            total += 1
            if total > 1:
                result += i
        else :
            total -= 1
            if total > 0:
                result += i
    return result


s1 = "(()())(())"
s2 = "(()())(())(()(()))"
s3 = "()()"
print(remove_outer_parentheses(s2))