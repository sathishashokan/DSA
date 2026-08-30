# Function to merge two halves
def merge(arr, low, mid, high):
    left = low
    right = mid+1
    temp = []
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        elif arr[left] > arr[right]:
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


def merge_sort(arr, low, high):
    if low == high:
        return
    mid = (low+high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

# Driver code
a = [4,5,1,3,2]
print(merge_sort(a, 0 , len(a)-1))
print(a)
