def binary_search(a, target, l, h):
    if l > h: # if element not in array
        return -1
    m = (l+h)//2
    if a[m] == target:
        return m
    if a[m] < target:
        return binary_search(a, target, m+1, h)
    return binary_search(a, target, l, m-1)



a = [1,2,3,4,5,6,7,8,9]
print(binary_search(a, 1, 0, len(a))) # function for returning the index of target