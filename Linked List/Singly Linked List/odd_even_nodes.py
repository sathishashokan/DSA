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

# keeping fast 2 step ahead, because if we keep the fast=head we'll lost track of the last element
def odd_even_nodes(head):
    if not head or not head.next:
        return head
    odd = head
    even_head = head.next
    even = head.next
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = even_head
    return head

arr = [1,2,3,4,5]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = odd_even_nodes(head)
print(printLL(head))