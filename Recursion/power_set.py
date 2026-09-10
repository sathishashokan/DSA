# Using take or ignore pattern using recursion
#         ""/abc
#         /     \
#       a/bc   ""/bc


def helper(p, up):
    if not up:
        res = [p]
        return res

    left = helper(p + up[0], up[1:])
    right = helper(p, up[1:])
    left.extend(right)
    return left


def possible_subseq(s):
    return helper("", s)


s = "abc"
print(possible_subseq(s))