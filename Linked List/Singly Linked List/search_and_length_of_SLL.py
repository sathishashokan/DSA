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

    def length(self, head):
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, head, node):
        temp = head
        while temp:
            if temp.data == node:
                return True
            temp = temp.next
        return False

if __name__ == "__main__":

    arr = [12,4,5,8]
    head = Node(arr[0])
    mover = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    sol = Solution()
    print(sol.printLL(head))
    print(sol.length(head))
    print(sol.search(head, 50))
