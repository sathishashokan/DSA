# printing the subsets of a string

def print_subseq(unprocessed, processed):
    if not unprocessed:
        print(processed) # printing the processed array when the unprocessed became empty
        return

    chr = unprocessed[0]
    print_subseq(unprocessed[1:], processed + chr) # add first char to processed array
    print_subseq(unprocessed[1:], processed) # ignore the first char

# returning the list of subsets of a string


def subseq_list(unprocessed, processed):
    if not unprocessed:
        res = [processed] # adding the processed array to a new list when the unprocessed became empty and returning it
        return res

    chr = unprocessed[0]
    left = subseq_list(unprocessed[1:], processed + chr) # add first char to processed array
    right = subseq_list(unprocessed[1:], processed) # ignore the first char
    left.extend(right)
    return left

# returning the list of subsets of a string and its ascii


def subseqAscii_list(unprocessed, processed):
    if not unprocessed:
        res = [processed] # adding the processed array to a new list when the unprocessed became empty and returning it
        return res

    chr = unprocessed[0]
    left = subseqAscii_list(unprocessed[1:], processed + chr) # add first char to processed array
    mid = subseqAscii_list(unprocessed[1:], processed + str(ord(chr))) # add ascii value of first char to processed array
    right = subseqAscii_list(unprocessed[1:], processed) # ignore the first char
    left.extend(mid)
    left.extend(right)
    return left


# using the concept used from recursion and implementing in iteration

import copy

def subset_list_iteration(arr):
    outer = [[]]
    for num in arr:
        for i in range(len(outer)):
            inner = outer[i].copy()
            # here we are taking the copy of only i'th inner list of the outer list(i.e copy of [] in [[]])
            # but if we take the copy of entire outer list, contains an inner mutable list, a normal shallow copy (like .copy() or [:]) will still share the reference to the inner list.
            inner.append(num)
            if inner not in outer: # to avoid duplicate subset
                outer.append(inner)
        # inner = copy.deepcopy(outer) # to take the  copy of entire outer list Use "copy.deepcopy()" from the standard copy module
        # for i in range(len(outer)):
        #     inner[i].append(num)
        # outer.extend(inner)
    return outer

s = "abc"
arr = [1,2,2]
# print(print_subseq(s, ""))
print(subset_list_iteration(arr))
