def is_array_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

arr = [11,2,9,3,7,4,8,5,6,10,1]
arr1 = [-1,-100,3,99]
arr2 = [1,2,3,4,4]
print(is_array_sorted(arr2))