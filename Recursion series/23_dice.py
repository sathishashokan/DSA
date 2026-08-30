def dice_combination(p, target):
    if target == 0:
        print(p)
        return
    for i in range(1,6 + 1):
        if i <= target: # to prevent sum of combination more than target
            dice_combination(p + str(i), target - i)


def dice_combination_list(p, target):
    if target == 0:
        res = [p]
        return res
    final = []
    for i in range(1,6 + 1):
        if i <= target: # to prevent sum of combination more than target
            final.extend(dice_combination_list(p + str(i), target - i))
    return final

def dice_with_diff_face_list(p, target, face):
    if target == 0:
        res = [p]
        return res
    final = []
    for i in range(1,face + 1):
        if i <= target: # to prevent sum of combination more than target
            final.extend(dice_with_diff_face_list(p + str(i), target - i, face))
    return final

dice_combination("", 4)
print(dice_combination_list("", 4))
print(dice_with_diff_face_list("", 7, 7))