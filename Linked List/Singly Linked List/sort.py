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

# find the middle 1
def middle(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(head1, head2):
    t1 = head1
    t2 = head2
    dummy_node = Node(-1)
    temp = dummy_node
    while t1 and t2:
        if t1.data < t2.data:
            temp.next = t1
            temp = t1
            t1 = t1.next
        else:
            temp.next = t2
            temp = t2
            t2 = t2.next

    temp.next = t1 if t1 else t2
    return dummy_node.next

def sort(head):
    if not head or not head.next:
        return head
    left = head
    middle1 = middle(head)
    right = middle1.next
    middle1.next = None

    left = sort(left)
    right = sort(right)

    return merge(left, right)


arr = [1,3,5,8,2,4,6,7,9]
head = convert_array_to_DLL(arr)
print(printLL(head))
head = sort(head)
print(printLL(head))