def remove_duplicate(arr):
    i = 0

    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    print(i)
    return arr

arr = [1,1,2,2,2,3,3]
arr1 = [2,2,2,3,3,3,3,4,4]
arr2 = [3,4,5,1,2]
print(remove_duplicate(arr1))