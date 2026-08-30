def find_index_of_element(arr, num):
    n = len(arr)
    for i in range(n):
        if arr[i] == num:
            return i
    return -1

arr = [1,2,3,4,5]
arr1 = [2,2,2,5,3,3,3,6,3,4,4]
arr2 = [1, 0, 2, 3,2,0,0,4,5,1]
print(find_index_of_element(arr, 3))