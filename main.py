# def insert_at_bottom(stack, temp):
#     if not stack:
#         stack.append(temp)
#         return
#
#     val = stack.pop()
#     insert_at_bottom(stack, temp)
#
#     stack.append(val)
#
#
# def reverse_stack(stack):
#     if stack:
#         temp = stack.pop()
#         reverse_stack(stack)
#         insert_at_bottom(stack, temp)


def minimumDeletions(nums):
    if len(nums) == 1:
        return 1

    small = 0
    large = 0

    for i, num in enumerate(nums):
        if num > nums[large]:
            large = i
        if num < nums[small]:
            small = i

    if small < large:
        res1 = large + 1
        res2 = len(nums) - small
        small += 1
        large = len(nums) - large
    else:
        res1 = small + 1
        res2 = len(nums) - large
        large += 1
        small = len(nums) - small

    res3 = small + large


    return min(res1, res2, res3)

nums = [2,10,7,5,4,1,8,6]
# nums = [0,-4,19,1,8,-2,-3,5]
print(minimumDeletions(nums))

# arr1 = [4,1,3,5]
# print(selection_main(arr1))
# print(arr1)
# print(total)
# stk = [4,3,1,2]
# stk1 = [10, 20, -5, 7, 15]
# reverse_stack(stk)
# print(stk)
