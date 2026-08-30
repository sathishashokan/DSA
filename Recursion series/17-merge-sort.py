def merge(arr, l, m, h):
    temp = []
    left = l
    right = m + 1
    while left <= m and right <= h:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        elif arr[right] < arr[left]:
            temp.append(arr[right])
            right += 1
    while left <= m:
        temp.append(arr[left])
        left += 1
    while right <= h:
        temp.append(arr[right])
        right += 1
    for i in range(len(temp)):
        arr[l+i] = temp[i]


def merge_sort(arr, l, h):
    if l>h:
        return
    # print(l, h)
    m = (l+h)//2
    if l < h:
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, h)
        merge(arr, l, m, h)


arr = [3,1,2]
merge_sort(arr, 0, len(arr) - 1)
print(arr)