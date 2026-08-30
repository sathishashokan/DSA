def reverse_array(arr,l,r):
    if l >= r:
        return arr
    arr[l], arr[r] = arr[r], arr[l]
    return reverse_array(arr, l+1,r-1)

def palindrome(s, n, i):
    if i >= n/2:
        return "palindrome"
    if s[i] != s[n-i-1]:
        return "not palindrome"
    return palindrome(s, n, i+1)



arr1 = [1,2,3,4,5]
n = len(arr1)
# print(reverse_array(arr1,0,n-1))
print(palindrome("uthra", 5, 0))