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
    current = head
    last = None
    while current:
        next = current.next
        current.next = last
        last = current
        current = next
    return last

def palindrome(head):
    if not head or not head.next:
        return True
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    new_head = reverse(slow.next)
    first = head
    second = new_head
    while second:
        if first.data != second.data:
            reverse(new_head)
            return False
        first = first.next
        second = second.next
    return True

arr = [1,2,3,4,5,6]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = palindrome(head)
print(printLL(head))