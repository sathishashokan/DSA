def union_of_two_array(arr1, arr2, m, n):
    i = 0
    j = 0
    union = []
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            if arr1[i] not in union:
                union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
                if arr2[j] not in union:
                    union.append(arr2[j])
                j += 1
        else:
            if arr1[i] not in union:
                union.append(arr1[i])
            i += 1
            j += 1

        print(f"union= {union}, i = {i}, j = {j}")
    while i < m:
        if arr1[i] not in union:
            union.append(arr1[i])
            i += 1

    while j < n:
        if arr2[j] not in union:
            union.append(arr2[j])
            j += 1

    return union



# arr = [0]
arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]
print(union_of_two_array(arr1, arr2, 10, 7))

