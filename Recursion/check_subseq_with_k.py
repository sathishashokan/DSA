def helper(p, up, k):
    if p == k:
        return True
    if not up:
        return False

    left = helper(p + up[0], up[1:], k)
    right = helper(p, up[1:], k)
    return left or right


def check_subseq_with_k(s, k):
    return helper(0, s, k)


s = [1, 2, 3, 4, 5]
s1 = [4, 3, 9, 2]

print(check_subseq_with_k(s, 8))
print(check_subseq_with_k(s1, 10))