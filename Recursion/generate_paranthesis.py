def helper(n, open_count, close_count, curr, res):
    if open_count == close_count == n:
        res.append(curr)
        return

    if open_count < n: # to add open parenthesis, it should be lesser than the given n
        helper(n, open_count + 1, close_count, curr + "(", res)
    if close_count < open_count: # to add close parenthesis, it should be lesser than the open parenthesis
        helper(n, open_count, close_count + 1, curr + ")", res)


def generate_parenthesis(n):
    res = []
    helper(n, 0, 0, "", res)
    return res


s = [1, 2, 3, 4, 5]
s1 = [4, 3, 9, 2]

print(generate_parenthesis(3))




