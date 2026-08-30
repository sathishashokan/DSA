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

def remove_duplicates(head):
    temp = head

    while temp and temp.next:
        next_node = temp.next

        while next_node and next_node.data == temp.data:
            next_node = next_node.next
        temp.next = next_node
        if next_node: next_node.prev = temp
        temp = temp.next
    return head


arr = [1,1,2,3,3,4,5]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = remove_duplicates(head)
print(printLL(head))
