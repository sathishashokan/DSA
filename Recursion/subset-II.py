# BRUTE APPROACH
# def sum_of_possible_subseq(arr):
#     res = []
#
#     def helper(arr, index, curr):
#         if index == len(arr):
#             res.append(curr)
#             return
#
#         helper(arr, index + 1, curr+[arr[index]])
#         helper(arr, index + 1, curr)
#
#     helper(arr, 0, [])
#     res.sort()
#     res_set = {tuple(sub) for sub in res}
#     res = [list(tup) for tup in res_set]
#
#     return res
#
# arr1 = [1,2,2]
# arr2 = [3,1,2]
# print(sum_of_possible_subseq(arr1))