# BINARY SEARCH
def find_peak(n):
    low = 1
    high = n
    ans = -1
    while low <= high:
        mid = (low+high)//2
        sqrt = mid * mid
        if sqrt == n:
            return mid
        if sqrt <= n:
            ans = mid # also high will always  end up in the answer
            low = mid + 1
        else:
            high = mid - 1
    return ans


def occurrence_of_element(n):
    index = find_peak(n)
    return index

# Driver code
a = [1,2,3,1]
b = [1,2,1,3,5,6,4]
c = [1,2,3,4,5,6,7,8,5,1]
print(occurrence_of_element(49))
