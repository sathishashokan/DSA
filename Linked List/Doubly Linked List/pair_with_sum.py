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

def delete_key(head, sum):
    left = head
    right = head
    result = []
    while right.next:
        right = right.next

    while left.data < right.data:
        total = left.data + right.data
        if total == sum:
            result.append([left.data, right.data])
            left = left.next
            right = right.prev
        elif total < sum:
            left = left.next
        else:
            right = right.prev
    return result

arr = [1,2,3,4,6]
head = convert_array_to_DLL(arr)
print(printLL(head))
print(delete_key(head, 5))
# head = delete_key(head, 5)
# print(printLL(head))