def selection_sort(arr, last_index, current_index, index_of_max):
    if last_index == 0:
        return

    if current_index < last_index:
        if arr[current_index] >= arr[index_of_max]:
            index_of_max = current_index
        return selection_sort(arr, last_index, current_index + 1, index_of_max)

    temp = arr[index_of_max]
    arr[index_of_max] = arr[last_index - 1]
    arr[last_index - 1] = temp
    return selection_sort(arr, last_index - 1, 0, 0)


def selection_main(arr):
    return selection_sort(arr, len(arr), 0, 0) # len(arr), because we need to check for the last element also


arr1 = [4,1,3,6,5]
print(selection_main(arr1))
print(arr1)