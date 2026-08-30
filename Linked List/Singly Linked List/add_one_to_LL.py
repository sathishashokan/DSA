class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data      # Data value
        self.next = next
        self.prev = prev

def convert_array_to_DLL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    back = head
    for i in range(1, len(arr)):
        temp = Node(arr[i], None, back)
        back.next = temp
        back = temp
    return head

def printLL(head):
    temp = head
    result = []
    while temp:
        result.append(temp.data)
        temp = temp.next
    return result

def helper(temp):
    if not temp:
        return 1
    carry = helper(temp.next)
    temp.data = temp.data + carry
    if temp.data < 10:
        return 0
    temp.data = 0
    return 1

def add_one_to_LL(head):
    temp = head
    carry = helper(temp)
    if carry == 1:
        new_head = Node(1)
        new_head.next = head
        return new_head
    return head

arr = [9,9,9]
arr2 = [1,5,9]
head = convert_array_to_DLL(arr2)
print(printLL(head))
head = add_one_to_LL(head)
print(printLL(head))