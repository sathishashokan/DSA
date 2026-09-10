def sum_subset_of_k(n, target):
    res = []

    def helper(index, curr_sum, curr_set):
        if len(curr_set) == n:
            if curr_sum == target:
                res.append(curr_set)
            return

        for i in range(index, 10):
            if curr_sum + i > target:
                break
            helper(i + 1, curr_sum + i, curr_set+[i])

    helper(1, 0, [])
    return res


k = 3
n = 9
print(sum_subset_of_k(k, n))