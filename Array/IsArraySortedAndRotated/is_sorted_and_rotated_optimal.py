def is_array_sorted_and_rotated(arr):
    n = len(arr)
    drop = 0
    for i in range(n):
        if arr[i-1] > arr[i]:
            drop += 1
    if drop > 1:
        return False
    else:
        return True

arr = [1,2,3]
arr1 = [2,1,3,4]
arr2 = [3,4,5,1,2]
print(is_array_sorted_and_rotated(arr))