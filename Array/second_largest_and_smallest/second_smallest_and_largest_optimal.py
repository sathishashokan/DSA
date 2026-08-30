def second_smallest_number(arr, n):
    if n < 2:
        return -1

    small = float('inf')
    second_small = float('inf')
    # arr = [1, 2, 4, 7, 7, 5]

    for i in range(n):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]

    return second_small

def second_largest_number(arr, n):
    if n < 2:
        return -1

    large = float('-inf')
    second_large = ('-inf')

    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]

    return second_large


arr = [1, 2, 4, 7, 7, 5]  # Array of elements
n = len(arr)

sS = second_smallest_number(arr, n)
sL = second_largest_number(arr, n)
print(sS)
print(sL)