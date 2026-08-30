# Using Dutch National Flag Algo:

def sort_array_of_0_1_2(arr):
    low, mid, high = 0, 0, len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


arr = [1,0,1,2,0]
arr1 = [0, 0, 1, 1, 1]
arr2 = [1,1,2,0]
arr3 = [0,2,0,2]
print(sort_array_of_0_1_2(arr))