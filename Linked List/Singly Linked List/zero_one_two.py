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

def zero_one_two(head):
    dummy_0 = Node(-1)
    dummy_1 = Node(-1)
    dummy_2 = Node(-1)
    zero = dummy_0
    one = dummy_1
    two = dummy_2
    temp = head
    while temp:
        data = temp.data
        if data == 0:
            zero.next = temp
            zero = temp
        elif data == 1:
            one.next = temp
            one = temp
        else:
            two.next = temp
            two = temp
        temp = temp.next
    zero.next = dummy_1.next if dummy_1.next else dummy_2.next
    one.next = dummy_2.next
    two.next = None
    return dummy_0.next

arr = [1,2,0,1,0,2]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = zero_one_two(head)
print(printLL(head))