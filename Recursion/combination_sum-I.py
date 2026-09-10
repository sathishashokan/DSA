def helper(arr, index, target, curr, res):
    if index == len(arr):
        if target == 0:
            res.append(list(curr))
        return
    if arr[index] <= target:
        curr.append(arr[index])
        helper(arr, index, target - arr[index], curr, res)
        curr.pop()
    helper(arr, index + 1, target, curr, res)


def combination_sum(arr, k):
    res = []
    curr = []
    helper(arr, 0, k, curr, res)
    return res

arr1 = [2,3,6,7]
arr2 = [2,3,5] # target = 8
print(combination_sum(arr1, 7))