# BINARY SEARCH

def min_days(bloom_day, day, m, k):
    count  = 0
    possible_bouquet = 0
    for num in bloom_day:
        if num <= day:
            count += 1
        else:
            possible_bouquet += (count//k)
            count = 0
    possible_bouquet += (count // k)
    return possible_bouquet >= m


def bouquet(bloom_day, m, k):
    if m*k > len(bloom_day):
        return -1
    low = min(bloom_day)
    high = max(bloom_day)
    while low <= high:
        mid = (low + high) // 2
        if min_days(bloom_day, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    return low


# Driver code
a = [1,10,3,10,2]
b = [7,7,7,7,12,7,7]
print(bouquet(a,3,1))
