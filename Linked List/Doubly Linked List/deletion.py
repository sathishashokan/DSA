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

def delete_head(head):
    if not head or head.next is None:
        return None
    temp = head
    head = head.next
    head.prev = None
    temp.next = None
    return head

def delete_tail(head):
    if not head or head.next is None:
        return None

    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.prev.next = None # Update second last node's next to None
    return head

def delete_k(head, k):
    if not head:
        return None
    temp = head
    count = 0
    while temp:
        count += 1
        if k == count:
            break
        temp = temp.next
    # If k is greater than the number of nodes
    if temp is None:
        return head
    prev = temp.prev
    next = temp.next
    if prev is None and next is None: #if true, this means it is a doubly linked list with only one node
        return None
    elif prev is None:
        return delete_head(head)
    elif next is None:
        return delete_tail(head)

    prev.next = next
    next.prev = prev
    return head

def delete_element(head, el):
    if not head:
        return None
    temp = head
    while temp:
        if el == temp.data:
            break
        temp = temp.next
    if temp is None: # If k is not present in the nodes
        return head
    prev = temp.prev
    next = temp.next
    if prev is None and next is None: #if true, this means it is a doubly linked list with only one node
        return None
    elif prev is None:
        return delete_head(head)
    elif next is None:
        return delete_tail(head)

    prev.next = next
    next.prev = prev
    return head



arr = [12,8,4,5]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = delete_element(head, 11)
print(printLL(head))