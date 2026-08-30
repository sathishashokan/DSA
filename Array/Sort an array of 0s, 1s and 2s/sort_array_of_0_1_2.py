def sort_array_of_0_1_2(arr):
    n = len(arr)
    count0, count1, count2  = 0, 0, 0

    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    index = 0
    for _ in range(count0):
        arr[index] = 0
        index += 1

    for _ in range(count1):
        arr[index] = 1
        index += 1

    for _ in range(count2):
        arr[index] = 2
        index += 1

arr = [1,0,1,2,0]
sort_array_of_0_1_2(arr)
print(arr)