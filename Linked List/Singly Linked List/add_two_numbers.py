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

def addTwoNumbers(l1, l2):
    dNode = Node(-1)
    current = dNode
    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.data
            l1 = l1.next
        if l2:
            sum += l2.data
            l2 = l2.next
        sum += carry
        carry = sum // 10

        new_node = Node(sum % 10)
        current.next = new_node
        current = new_node
    return dNode.next


arr = [9,9,9]
arr2 = [9,9]
head1 = convert_array_to_DLL(arr)
head2 = convert_array_to_DLL(arr2)
print(printLL(head1))
print(printLL(head2))
head = addTwoNumbers(head1, head2)
print(printLL(head))
