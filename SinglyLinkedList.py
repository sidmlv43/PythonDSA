class Node:
    """
    Node represent a single node of a link list.
    It consists of a data value and a reference to next Node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    """
    Linked List is similar to a list which is used to store multiple data in a single variable.
    It consists of a Head Node and Tail node.
    Head will represent the starting of a Linked list.
    while Tail will always point to None and helps to add a new node in the end of Linked List.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self._size += 1
            return
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self._size += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self._size += 1

    def add(self, data, idx=None):
        if idx is None:
            self.add_last(data)
            return
        if idx == 0:
            self.add_first(data)
            return
        new_node = Node(data)
        i = 0
        curr = self.head
        while i < idx - 1:
            curr = curr.next
            i += 1
        new_node.next = curr.next
        curr.next = new_node
        self._size += 1

    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last(self):
        """

        :return:Nothing
        Removes last node
        """
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        curr.next = None
        self.tail = curr
        self._size -= 1

    def remove(self, idx=None):
        """

        :param idx: index of node
        :return: Nothing
        it removes ith node from start, if no index provided, it removes last node
        """
        if idx is None or idx == self._size - 1:
            self.remove_last()
            return

        if idx == 0:
            self.remove_first()
            return
        i = 0
        cur = self.head
        while i < idx - 1:
            cur = cur.next
            i += 1

        cur.next = cur.next.next
        self._size -= 1

    def remove_nth_from_end(self, n):
        """

        :param n:
        :return: deletes ith node from end
        """
        if n == self._size:
            self.remove_first()
            return
        i = 1
        i_to_find = self._size - n
        prev = self.head
        while i < i_to_find:
            prev = prev.next
            i += 1
        prev.next = not prev.next
        self._size -= 1

    def reverse(self):
        """

        :return: reverse of linked list
        """
        prev = None
        curr = self.tail = self.head
        # nxt = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    @classmethod
    def get_mid(cls, source):
        """

        :param source: source is an instance of a Node class.
        :return: returns a reference of a middle node.
        """

        slow = source
        fast = source.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    @classmethod
    def merge(cls, left, right):
        """

        :param left:
        :param right:
        :return: merges both linked list in a sorted manner and return the head of LL.
        """
        merged = Node(-1)
        temp = merged
        while left is not None and right is not None:
            if left.data <= right.data:
                temp.next = left
                temp = temp.next
                left = left.next
            else:
                temp.next = right
                temp = temp.next
                right = right.next
        while left is not None:
            temp.next = left
            temp = temp.next
            left = left.next
        while right is not None:
            temp.next = right
            temp = temp.next
            right = right.next

        return merged.next

    def merge_sort(self, head=None):
        """

        :param head:
        :return: sort the linked list and return a new head with the smallest value
        """

        if head is None:
            head = self.head
        if head is None or head.next is None:
            return head
        #     get the mid of ll
        mid_node = LinkedList.get_mid(head)
        right_head = mid_node.next
        mid_node.next = None

        new_left = self.merge_sort(head)
        new_right = self.merge_sort(right_head)

        return LinkedList.merge(new_left, new_right)

    def length(self):
        return self._size

    def __str__(self):
        rep = ""
        curr = self.head
        while curr is not None:
            rep += (str(curr.data) + "-> ")
            curr = curr.next
        # rep += curr.next
        rep += "null"
        return rep


if __name__ == '__main__':
    # print(LinkedList.__doc__)
    ll = LinkedList()
    ll.add_first(1)
    ll.add_first(2)
    ll.add_first(3)
    ll.add_first(4)
    ll.add_first(5)
    ll.add_first(6)
    ll.add_first(7)
    ll.add_first(8)
    # ll.add_first(10)
    ll.add_first(33)

    print(ll)

    ll.head = ll.merge_sort(ll.head)
    # ll.reverse()
    print(ll)
    print(ll.merge_sort.__doc__)
