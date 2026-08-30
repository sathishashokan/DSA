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


def removeNthFromEnd(head, n):
    fast = head
    for i in range(n):
        fast = fast.next
    if not fast:
        return head.next
    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head

arr = [1,2,3,4,5]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = removeNthFromEnd(head, 4)
print(printLL(head))