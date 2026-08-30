def remove_duplicate(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i+1]:
            arr.remove(arr[i])
            arr.append("_")
        else:
            i += 1

        if arr[i] == "_":
            break

    return arr

arr = [1,1,2,2,2,3,3]
arr1 = [2,1,3,4]
arr2 = [3,4,5,1,2]
print(remove_duplicate(arr))