# BRUTE FORCE
# sort the array and check if the next element to the current element(x) is x+1
# if yes, count ++ and check max. Finally return max

def longest_sequence(nums):
    # convert to set
    new_set = set(nums)
    maxi = 0

    for s in new_set:
        x = s
        if x-1 not in new_set:
            count = 1
            while x+1 in new_set:
                x += 1
                count += 1
            maxi = max(maxi, count)
    return maxi

arr = [100, 4, 200, 1, 3, 2] # n = 6
arr1 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] # n = 10
arr2 = [1,2,4,4,5,6,8]
print(longest_sequence(arr1))
