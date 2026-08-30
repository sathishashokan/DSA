def bubble_sort(arr, last_index, current_index):
    if last_index == 0:
        return
    if current_index < last_index:
        if arr[current_index] > arr[current_index + 1]:
            temp = arr[current_index]
            arr[current_index] = arr[current_index + 1]
            arr[current_index + 1] = temp
        bubble_sort(arr, last_index, current_index + 1)
    bubble_sort(arr, last_index - 1, 0)


def bubble_main(arr):
    return bubble_sort(arr, len(arr)-1, 0)


arr1 = [4,1,3,6,5]
print(bubble_main(arr1))
print(arr1)