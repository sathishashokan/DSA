def helper(p, up, k):
    if p == k:
        return 1
    if not up:
        return 0

    left = helper(p + up[0], up[1:], k)
    right = helper(p, up[1:], k)
    return left + right


def count_of_subseq_with_k(s, k):
    return helper(0, s, k)


s = [4,9,2,5,1]
s1 = [4, 2, 10, 5, 1, 3]

print(count_of_subseq_with_k(s1, 5))