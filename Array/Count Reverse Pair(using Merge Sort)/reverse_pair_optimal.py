# Function to merge two halves
def merge(arr, low, mid, high):
    left = low
    right = mid+1
    temp = []
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
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

def count_reverse_pair(arr, low, mid, high):
    count = 0
    right = mid + 1
    print(arr)
    for i in range(low, mid+1):
        while right <= high and arr[i] > 2*arr[right]:
            # print(f"({arr[i], arr[right], right}")
            right += 1
            # print(f"({right, mid, count}")
        count += (right-(mid+1))
        print(count)
        # print(f"count = {count}")
    return count

def merge_sort(arr, low, high):
    count = 0
    if low == high:
        return 0
    mid = (low+high)//2
    count += merge_sort(arr, low, mid)
    # print(f"c1 = {count}")
    count += merge_sort(arr, mid+1, high)
    # print(f"c2 = {count}")
    count += count_reverse_pair(arr, low, mid, high)
    # print(f"c3 = {count}")
    merge(arr, low, mid, high)
    return count

# Driver code
a = [2,4,3,5,1]
print(merge_sort(a, 0 , len(a)-1))
# print(a)
