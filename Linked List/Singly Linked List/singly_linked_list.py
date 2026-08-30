class Node:
    def __init__(self, data, next=None):
        self.data = data      # Data value
        self.next = next      # Pointer to next node

    def insert(self, head, value):
        # temp = head
        # temp.next = head.next
        head = Node(value, head)
        return head


# Driver code
if __name__ == "__main__":
    # Create an array
    arr = [12, 5, 8, 7]

    # Create first node
    head = Node(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    # Print memory reference of node
    # print(head)
    #
    # # Print data stored in node
    # print(head.data)
    # print(head.next)

    # Traversal
    temp = head
    count  = 0
    print("Before new head")
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
        count += 1
    print(count)
    head = head.insert(head, 10)
    print("After new head")
    temp = head
    count = 0
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
        count += 1
    print(count)