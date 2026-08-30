def element_appeared_once(arr):
    xor = 0

    for num in arr:
        xor ^= num
    return xor

arr = [2, 2, 1]
arr1 = [1,1,2,2,3,3,4]
arr2 = [4,1,2,1,2]
arr3 = [4,1,2,4,1,2,3]
print(element_appeared_once(arr))