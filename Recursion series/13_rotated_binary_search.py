def rotated_binary_search(arr, target, l, h):
    if l > h:
        return -1
    m = (l+h)//2
    if arr[m] == target:
        return m
    if arr[l] <= arr[m]:
        if arr[l] <= target <= arr[m]:
            return rotated_binary_search(arr, target,l, m - 1)
        else:
            return rotated_binary_search(arr, target,m+1, h)
    else:
        if arr[m+1] <= target <= arr[h]:
            return rotated_binary_search(arr, target,m+1, h)
        else:
            return rotated_binary_search(arr, target,l, m - 1)



arr = [5,6,7,1,2,3]
print(rotated_binary_search(arr, 70, 0, len(arr)-1))