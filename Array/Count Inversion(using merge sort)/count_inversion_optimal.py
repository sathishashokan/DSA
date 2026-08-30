# Function to merge two halves
def merge(arr, low, mid, high):
    inversion_count = 0
    left = low
    right = mid+1
    temp = []
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        elif arr[left] > arr[right]:
            inversion_count += (mid-left+1)
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = temp[i-low]
    return inversion_count


def merge_sort(arr, low, high):
    count = 0
    if low == high:
        return 0
    mid = (low+high)//2
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid+1, high)
    count += merge(arr, low, mid, high)
    return count

# Driver code
a = [5,4,3,2,1]
print(merge_sort(a, 0 , len(a)-1))
