def rotate_left_by_one(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(0, n - 1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    return arr

def rotate_right_by_one(arr):
    # [1,2,3,4,5]
    # [5,1,2,3,4]
    n = len(arr)
    temp = arr[-1]

    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr

arr = [1,1,2,2,2,3,3]
arr1 = [1,2,3,4,5]
arr2 = [-10,100,8,12]
print(rotate_right_by_one(arr1))