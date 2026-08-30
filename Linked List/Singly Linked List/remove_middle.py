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

# keeping fast 2 step ahead, because if we keep the fast=head we'll lost track of the last element
def remove_middle(head):
    if not head or not head.next:
        return None
    slow = head
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return head

# def remove_middle(head):
    if not head or not head.next:
        return None
    slow = head
    fast = head
    last = None
    while fast and fast.next:
        last = slow
        slow = slow.next
        fast = fast.next.next
    last.next = last.next.next
    return head

arr = [1,2,3,4,5]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = remove_middle(head)
print(printLL(head))