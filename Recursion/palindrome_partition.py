def palindrome_partition(s):
    res = []

    def helper(s, index, curr):
        if index == len(s):
            res.append(curr)
            return

        for i in range(index, len(s)):
            if is_palindrome(s, index, i):
                helper(s, i + 1, curr + [s[index:i+1]])

    def is_palindrome(s, start, end):
        # sub = s[start:end+1]
        # return sub == sub[::-1]
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    helper(s, 0, [])
    return res


s = "aabb"
print(palindrome_partition(s))