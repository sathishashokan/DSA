def helper(arr, index, k, curr, res):
    if k == 0:
        res.append(list(curr))
        return
    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i-1]:
            continue
        if arr[i] > k:
            break
        curr.append(arr[i])
        helper(arr, i + 1, k - arr[i], curr, res)
        curr.pop()


def combination_sum(arr, target):
    res, curr = [], []
    arr.sort()
    helper(arr, 0, target, curr, res)
    return res

arr1 = [2, 5, 6]
arr2 = [10,1,2,7,6,1,5]
arr3 = [2,5,2,1,2]
print(combination_sum(arr2, 8))