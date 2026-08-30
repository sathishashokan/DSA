# Input:
#  arr[] = {2, 5, 1, 3, 0}
# Output:
#  5

# solution 1:
# def largest_element_array(arr):
#     i = 0
#     j = 0
#     while j != len(arr):
#         if arr[i] < arr[j]:
#             i = j
#         j += 1
#
#     return arr[i]
#
# a = [8, 10, 5, 7, 9]
# print(largest_element_array(a))

# solution 2:
def largest_element_array(arr):
    max_value = arr[0] # Initialize max with the first element in the array

    # Iterate through the array to find the maximum element
    for i in range(1, len(arr)):
        if max_value < arr[i]: # If the current element is greater than max, update max
            max_value = arr[i]

    return max_value # Return the largest element found

arr1 = [2, 5, 1, 3, 0]
arr2 = [8, 10, 5, 7, 9]
print(largest_element_array(arr1)) # Call the function to find the largest element and Output the result
print(largest_element_array(arr2)) # Call the function to find the largest element and Output the result
