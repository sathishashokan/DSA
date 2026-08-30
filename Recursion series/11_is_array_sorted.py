def is_array_sorted(arr, i):
    if i == len(arr)-1:
        return True
    return arr[i] < arr[i+1] and is_array_sorted(arr, i+1)

arr = [1,2,3,4,5]
print(is_array_sorted(arr, 0))