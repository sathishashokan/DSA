def subseq_with_sum(p, up, k):
    if not up:
        if sum(p) == k:
            print(p)
        return

    new_p = p.copy()
    for num in up:
        new_p.append(num)
        subseq_with_sum(new_p, up[1:], k)
        if p:
            subseq_with_sum(p, up[1:], k)


nums = [4, 9, 2, 5, 1]
subseq_with_sum([], nums, 10)