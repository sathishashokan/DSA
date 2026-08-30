def permutation(p, up):
    if not up:
        print(p)
        return
    ch = up[0]
    for i in range(len(p)+1):
        first = p[0:i]
        second = p[i:]
        permutation(first + ch + second, up[1:])

def permutation_list(p, up):
    if not up:
        res = [p]
        return res
    ch = up[0]
    final = []
    for i in range(len(p)+1):
        first = p[0:i]
        second = p[i:]
        final.extend(permutation_list(first + ch + second, up[1:]))
    return final

def count_of_permutation(p, up):
    if not up:
        return 1
    ch = up[0]
    count = 0
    for i in range(len(p)+1):
        first = p[0:i]
        second = p[i:]
        count += count_of_permutation(first + ch + second, up[1:])
    return count



s = "abc"
permutation("", s)
print(permutation_list("", s))
print(count_of_permutation("", s))