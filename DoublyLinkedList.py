class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def _reset_tail(self):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        self.tail = curr

    def add_first(self, data):
        new_node = _Node(data)
        self._size += 1
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_last(self, data):
        new_node = _Node(data)
        self._size += 1
        if self.head is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def remove_first(self):
        if self._size == 1:
            self._size = 0
            self.head = self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None
        self._size -= 1

    def remove_last(self):
        if self._size == 1:
            self._size = 0
            self.head = self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
        self._size -= 1

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            curr.prev = nxt

            prev = curr
            curr = nxt

        self.head = prev
        self._reset_tail()

    def __str__(self):
        if self._size == 0:
            return "null"
        rep = ""
        cur = self.head
        while cur.next is not None:
            rep += (str(cur.data) + "<->")
            cur = cur.next
        rep += str(cur.data)
        rep += "->null"
        return rep


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.add_first(12)
    dll.add_first(2)
    dll.add_first(7)
    dll.add_first(9)
    print(dll)

    dll.reverse()
    print(dll)

    print(dll.head.data)
    print(dll.tail.data)
