# BINARY SEARCH
from math import ceil

def piles_per_hour(piles, h):
    low = 1
    high = max(piles)
    while low <= high:
        mid = (low + high) // 2
        k = 0
        for pile in piles:
            k += ceil(pile / mid)
        if k <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low


# Driver code
a = [3,6,7,11]
b = [312884470]
print(piles_per_hour(b,312884469))
