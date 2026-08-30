def sec_lar_and_small(arr, n):
    max_value = float('-inf')
    min_value = float('inf')
    sec_lar = float('-inf')
    sec_small = float('inf')

    for i in range(n):
        if arr[i] > max_value:
            max_value = arr[i]
        if arr[i] < min_value:
            min_value = arr[i]

    for i in range(n):
        if arr[i] != max_value and arr[i] > sec_lar:
            sec_lar = arr[i]
        if arr[i] != min_value and arr[i] < sec_small:
            sec_small = arr[i]

    print("Second smallest is", sec_small)
    print("Second largest is", sec_lar)


arr1 = [7, 2, 1, 6, 4, 8, 5, 7, 8, 8, 7]
print(sec_lar_and_small(arr1, len(arr1)))