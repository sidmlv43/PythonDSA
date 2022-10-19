class Node:
    """
    Node class emulates a linked list
    it consists of a data and a reference to the next node

    _________Usage_________

    new_node = Node(1)
    """
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    """
    Stack is a linear data structure which follows a particular order in which the operations are performed.
    The order may be LIFO(Last In First Out) or FILO(First In Last Out)
                                                                                        source - GFG
    """
    def __init__(self):
        self._head = None

    def is_empty(self):
        """

        :return: True if the stack is empty else returns False
        """
        return self._head is None

    def push(self, data: int) -> None:
        """

        :param data:
        :return:
        """
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            return
        new_node.next = self._head
        self._head = new_node

    def peek(self) -> int:
        """

        :return: top node of the stack
        """
        return self._head.data

    def pop(self) -> int:
        """

        :return: removed top node
        """
        top = self._head
        self._head = self._head.next
        return top.data

    def _push_bottom_func(self, new_node):
        """

        :param new_node: instance of Node class
        :return: None, pushes the node to the bottom of Stack
        """
        if self.is_empty():
            self.push(new_node)
            return
        top = self.pop()
        self.push_bottom(new_node)
        self.push(top)

    def push_bottom(self, data):
        """

        :param data:
        :return: None
        a helper function for users to pass primitive values to the bottom of Stack.
        """
        new_node = Node(data)
        self._push_bottom_func(new_node)

    def reverse(self):
        """

        :return: None, reverse the stack and returns a new head
        """
        if self.is_empty():
            return
        top = self.pop()
        self.reverse()
        self._push_bottom_func(top)


if __name__ == '__main__':
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push_bottom(0)

    s.reverse()

    while not s.is_empty():
        print(s.pop())

    print(Node.__doc__)
    print(Stack.__doc__)
