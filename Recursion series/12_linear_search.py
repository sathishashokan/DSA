# Example of using linear search using recursion


def find_first_index(arr, index, target):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return find_first_index(arr, index+1, target)

def find_last_index(arr, index, target):
    if index == -1:
        return -1
    if arr[index] == target:
        return index
    return find_first_index(arr, index - 1, target)

def find_all_occurrence(arr, index, target, result):
    if index == len(arr):
        return result
    if arr[index] == target:
        result.append(index)
    return find_all_occurrence(arr, index+1, target, result)

# same problem but without passing additional argument
def find_every_occurrence(arr, index, target):
    result = []
    if index == len(arr):
        return result
    if arr[index] == target:
        result.append(index)
    result.extend(find_every_occurrence(arr, index+1, target))
    return result



arr = [1, 2, 4, 3, 4, 4, 5]
print(find_first_index(arr, 0, 4))
print(find_last_index(arr, len(arr) - 1, 4))
print(find_all_occurrence(arr, 0, 4, []))
print(find_every_occurrence(arr, 0, 4))