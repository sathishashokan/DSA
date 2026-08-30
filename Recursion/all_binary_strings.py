# generate binary strings of length n that do not contain consecutive 1s

#Approach 1: storing in list inside each function and passing to above function or where it was called

# def all_binary_of_n(p, up):
#     if up == 0:
#         res = [p]
#         return res
#
#     final_res = []
#     final_res.extend(all_binary_of_n(p + "0", up - 1))
#     if not p or not p[-1] == "1":
#         final_res.extend(all_binary_of_n(p + "1", up - 1))
#     return final_res


# Approach 2: passing in argument

def all_binary_of_n(p, up, res):
    if up == 0:
        res.append(p)
        return

    all_binary_of_n(p + "0", up - 1, res)
    if not p or not p[-1] == "1":
        all_binary_of_n(p + "1", up - 1, res)

res = []
print(all_binary_of_n("", 3, res))
print(res)