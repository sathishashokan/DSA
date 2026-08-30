# MY BRUTE FORCE

# def merge_intervals(intervals):
#     n = len(intervals)
#     intervals.sort()
#     res = []
#     for i in range(n-1):
#         curr_sub = intervals[i]
#         j = i + 1
#         if res and res[-1][-1] >= curr_sub[-1]:
#             continue
#         while intervals[j][0] < curr_sub[-1] < intervals[j][1]:
#             curr_sub[-1] = intervals[j][-1]
#             j += 1
#         res.append(curr_sub)
#     return res

# BRUTE FORCE

# def merge_intervals(intervals):
#     n = len(intervals)
#     intervals.sort()
#     res = []
#     i = 0
#     while i < n:
#         start = intervals[i][0]
#         end = intervals[i][1]
#         j = i+1
#         while j < n and intervals[j][0] <= end:
#             end = max(end, intervals[j][1])
#             j += 1
#         i = j
#         res.append([start, end])
#     return res

def merge_intervals(intervals):
    intervals.sort()
    res = []
    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return res


arr = [[1,3],[2,6],[8,10],[15,18], [16,17]]
arr1 = [[1,4],[4,5]]
arr2 = [[4,7],[1,4]]
arr3 = [[1,3],[2,4],[2,6],[8,9],[8,10],[9,11],[15,18],[16,17]]
print(merge_intervals(arr3))
