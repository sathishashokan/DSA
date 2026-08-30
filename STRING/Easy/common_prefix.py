# MY APPROACH
# def common_prefix(s):
    # small_str = min(s, key=lambda x:len(x))
    # result = ""
    # for i in range(len(small_str)):
    #     count = 0
    #     for j in range(len(s)):
    #         if small_str[i] == s[j][i]:
    #             count += 1
    #     if count == len(s):
    #         result += small_str[i]
    # return result

# Leet code Approach
def common_prefix(s):
    s.sort()
    result = ""
    # comparing first and last subarrays
    for i in range(min(len(s[0]),len(s[-1]))):
        if s[0][i] == s[-1][i]:
            result += s[0][i]
        else:
            break
    return result


s1 = ["flower", "flow", "flight"]
s2 = ["dog","racecar","car"]
print(common_prefix(s1))