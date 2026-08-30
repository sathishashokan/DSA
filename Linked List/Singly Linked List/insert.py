class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:

    def printLL(self, head):
        temp = head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    def insert_new_head(self, head, value):
        return Node(value, head)

    def insert_at_tail(self, head, value):
        if not head:
            return Node(value)
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(value)
        return head

    def insert_at_k(self, head, value, k):
        if not head:
            if k == 1:
                return Node(value)
            else:
                return None
        if k == 1:
            return Node(value, head)
        temp = head
        count = 0
        while temp:
            count += 1
            if k-1 == count:
                new_node = Node(value, temp.next)
                temp.next = new_node
                break
            temp = temp.next
        return head

    def insert_before_el(self, head, value, el):
        if not head:
            return None # if head is null, we can't find any element to insert the value before it
        if head.data == el:
            return Node(value, head)
        temp = head
        while temp.next is not None:
            if temp.next.data == el:
                new_node = Node(value, temp.next)
                temp.next = new_node
                break
            temp = temp.next
        return head


if __name__ == "__main__":

    arr = [12,4,5,8]
    head = Node(arr[0])
    mover = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    sol = Solution()
    # print(f"before adding new head {sol.printLL(head)}")
    # head = sol.insert_new_head(head, 10)
    # print(f"after adding new head {sol.printLL(head)}")
    # print(f"before adding at tail {sol.printLL(head)}")
    # head = sol.insert_at_tail(head, 10)
    # print(f"after adding at tail {sol.printLL(head)}")
    # print(f"before adding at k {sol.printLL(head)}")
    # head = sol.insert_at_k(head, 10, 4)
    # print(f"after adding at k {sol.printLL(head)}")
    print(f"before adding before element {sol.printLL(head)}")
    head = sol.insert_before_el(head, 10, 6)
    print(f"after adding before element {sol.printLL(head)}")