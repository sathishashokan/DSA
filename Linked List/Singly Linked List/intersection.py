def getIntersectionNode(headA,headB):
    t1 = headA
    t2 = headB

    while t1 != t2:
        t1 = t1.next if t1 else headB
        t2 = t2.next if t2 else headA

    return t1

# This program will not run, For reference purpose only

arr1 = [1,2,3,4,5,6]
arr2 = [7,8,9,4,5,6]