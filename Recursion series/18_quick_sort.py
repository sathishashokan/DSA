def quick_sort(arr, l, h):
    if l >= h:
        return

    s = l
    e = h
    m = (l+h)//2
    pivot = arr[m]

    while s <= e:
        while arr[s] < pivot:
            s += 1
        while arr[e] > pivot:
            e -= 1
        temp = arr[s]
        arr[s] = arr[e]
        arr[e] = temp
        s += 1
        e -= 1

    quick_sort(arr, l, e)
    quick_sort(arr, s, h)


a = [5,2,4,3,1]
quick_sort(a, 0, len(a)-1)
print(a)