def sum_of_possible_subseq(p, up):
    if not up:
        res = [sum(p)]
        return res

    left = sum_of_possible_subseq(p, up[1:])
    right = sum_of_possible_subseq(p + [up[0]], up[1:])
    left.extend(right)
    left.sort()
    return left


arr1 = [5,2,1]
arr2 = [3,1,2]
print(sum_of_possible_subseq([], arr1))