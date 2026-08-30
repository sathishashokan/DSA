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

def insert_before_head(head, value):
    new_head = Node(value, head, None)
    head.prev = new_head
    return new_head

def insert_before_tail(head, value):
    if head.next is None:
        return insert_before_head(head, value)

    temp = head
    while temp.next:
        temp = temp.next
    back = temp.prev
    new_node = Node(value, temp, back)
    back.next = new_node
    temp.prev = new_node
    return head

def insert_before_k(head, value, k):
    if not head:
        return None
    if k == 1:
        return insert_before_head(head, value)

    temp = head
    count = 0
    while temp:
        count += 1
        if count == k: break
        temp = temp.next
    if temp is None: # If k is greater than the number of nodes
        return head
    back = temp.prev
    new_node = Node(value, temp, back)
    back.next = temp.prev = new_node
    return head

def insert_before_element(head, value, el):
    if not head:
        return None
    if el == head.data:
        return insert_before_head(head, value)

    temp = head
    while temp:
        if temp.data == el: break
        temp = temp.next
    if temp is None: # If k is not present in the nodes
        return head
    back = temp.prev
    new_node = Node(value, temp, back)
    back.next = temp.prev = new_node
    return head


arr = [12,8,4,5]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = insert_before_element(head, 111, 8)
print(printLL(head))