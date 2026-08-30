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

# def delete_head(head):
#     temp = head
#     head = head.next
#     head.prev = None
#     return head
#
#
# def delete_key(head, k):
#     if not head or not head.next:
#         return None
#
#     current = head
#     while current:
#         if current.data == k:
#             prev = current.prev
#             next = current.next
#             if prev is None:
#                 head = delete_head(head)
#                 current = head
#                 continue
#             elif next is None:
#                 current.prev.next = None
#                 # break
#             else:
#                 prev.next = next
#                 next.prev = prev
#         current = current.next
#     return head

# Striver Approach

def delete_key(head, k):
    temp = head

    while temp:
        if temp.data == k:
            if temp == head:
                head = temp.next
            prev = temp.prev
            next = temp.next
            if prev: prev.next = next
            if next: next.prev = prev
            temp = next
        else:
            temp = temp.next
    return head

arr = [1,2,3,1,4,1]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = delete_key(head, 1)
print(printLL(head))