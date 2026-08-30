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

    @staticmethod
    def delete_head(head):
        new_head = head.next
        head.next = None # detach old head to help garbage collection
        return new_head

    @staticmethod
    def delete_tails(head):
        current = head
        while current.next.next is not None:
            current = current.next
        current.next = None
        return head

    @staticmethod
    def delete_k(head, k):
        if not head:
            return head
        if k == 1:
            new_head = head.next
            head.next = None
            return new_head
        temp = head
        count = 0
        prev = None
        while temp:
            count += 1
            if k == count:
                prev.next = prev.next.next
                break
            prev = temp
            temp = temp.next
        return head

    @staticmethod
    def delete_element(head, element):
        if not head:
            return head
        if head.data == element:
            new_head = head.next
            head.next = None
            return new_head
        temp = head
        prev = None
        while temp:
            if temp.data == element:
                prev.next = prev.next.next
                break
            prev = temp
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
    # print(f"before deleting head {sol.printLL(head)}")
    # head = sol.delete_head(head)
    # print(f"after deleting head {sol.printLL(head)}")
    # print(f"before deleting tail {sol.printLL(head)}")
    # sol.delete_tails(head)
    # print(f"after deleting tail {sol.printLL(head)}")
    # print(f"before deleting kth {sol.printLL(head)}")
    # head = sol.delete_k(head, 8)
    # print(f"after deleting kth {sol.printLL(head)}")
    print(f"before deleting element {sol.printLL(head)}")
    head = sol.delete_element(head, 8)
    print(f"after deleting element {sol.printLL(head)}")
