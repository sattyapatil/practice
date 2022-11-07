class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


li = LinkedList()

li.head = Node(10)

second = Node(20)

li.head.next = second

second.next = Node(30)

while li.head:
    print(li.head.data)
    li.head = li.head.next

