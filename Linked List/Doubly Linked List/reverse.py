class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data      # Data value
        self.next = next
        self.prev = prev

def convert_array_to_DLL(arr):
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

def reverse(head):
    # My Approach
    # temp = head
    # while temp:
    #     temp.next, temp.prev = temp.prev, temp.next
    #     if temp.prev is None:
    #         break
    #     temp = temp.prev
    # return temp

    # striver's Approach
    temp = None
    current = head
    while current:
        temp = current.prev # storing prev value because it will be overwritten in the next line
        current.prev = current.next
        current.next = temp
        current = current.prev
    if temp is not None:
        head = temp.prev
    return head



arr = [12,8,4,5]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = reverse(head)
print(printLL(head))