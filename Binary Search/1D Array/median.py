# BETTER APPROACH
# def median(num1, num2):
#     m = len(num1)
#     n = len(num2)
#     index2 = (m+n)//2
#     index1 = index2 - 1
#     el1, el2 = -1, -1
#     count = 0
#     i,j = 0,0
#
#     while i<m and j<n:
#         if num1[i] < num2[j]:
#             if count == index1:
#                 el1 = num1[i]
#             if count == index2:
#                 el2 = num1[i]
#             count += 1
#             i += 1
#         else:
#             if count == index1:
#                 el1 = num2[j]
#             if count == index2:
#                 el2 = num2[j]
#             count += 1
#             j += 1
#     while i<m:
#         if num1[i] < num2[j]:
#             if count == index1:
#                 el1 = num1[i]
#             if count == index2:
#                 el2 = num1[i]
#             count += 1
#             i += 1
#     while j<n:
#         if count == index1:
#             el1 = num2[j]
#         if count == index2:
#             el2 = num2[j]
#         count += 1
#         j += 1
#     if (m+n)%2==0:
#         return (el1+el2)/2
#     else:
#         return el2

# OPTIMAL APPROACH(BINARY SEARCH)
def median(num1, num2):
    n1 = len(num1)
    n2 = len(num2)
    n = n1+n2
    # Ensure nums1 is the smaller array for simplicity
    if n1 > n2:
        return median(num2, num1)
    low = 0
    high = n1
    while low <= high:
        mid1 = (low+high)//2
        mid2 = (n1+n2+1)//2 - mid1
        print(mid1, mid2)
        l1 = l2 = float('-inf')
        r1 = r2 = float('inf')
        if mid1 < n1:
            r1 = num1[mid1]
        if mid2 < n2:
            r2 = num2[mid2]
        if (mid1-1) >= 0:
            l1 = num1[mid1 - 1]
        if (mid2-1) >= 0:
            l2 = num2[mid2 - 1]
        print(r1, r2, l1, l2)
        print("-------------------------------")
        if l1 <= r2 and l2 <= r1:
            if n%2==0:
                return (max(l1,l2) + min(r1,r2))/2.0
            else:
                return max(l1,l2)
        elif l1 > r2:
            high = mid1 - 1
            print(high)
        else:
            low = mid1 + 1


# Driver code
a = [1,3]
b = [2]
print(median(a,b))
