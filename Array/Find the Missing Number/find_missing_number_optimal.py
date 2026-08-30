def find_missing_number(arr):
    n = len(arr) + 1# 8
    hash = [0] * (n + 1) # 9

    for i in range(n - 1): # 7
        hash[arr[i]] += 1

    for i in range(1, n + 1):
        if hash[i] == 0:
            return i
    return hash



# arr = [0]
arr1 = [1,2,3,5,6,7,8,9,10]
arr2 = [8, 2, 4, 5, 3, 7, 1]
print(find_missing_number(arr2))