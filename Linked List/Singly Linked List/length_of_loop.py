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

def split_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            fast = fast.next
            count = 1
            while slow != fast:
                fast = fast.next
                count += 1
            return count
    return 0


arr = [1,2,3,4,5,6]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = reverse_SLL(head)
print(printLL(head))