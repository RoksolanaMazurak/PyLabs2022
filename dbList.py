from employee import Employee


class Dblist:
    class Node:
        previous = None
        next = None
        element = None

        def __init__(self, element: Employee, next_node=None, previous_node=None) -> None:
            self.element = element
            self.next = next_node
            self.previous = previous_node

    head = None
    tail = None
    length = 0

    def add(self, element):
        self.length += 1
        if not self.head:
            self.head = self.Node(element)
            return element
        elif not self.tail:
            self.tail = self.Node(element, None, self.head)
            self.head.next = self.tail
            return element
        else:
            self.tail = self.Node(element, None, self.tail)
            self.tail.previous.next = self.tail
            return element

    def add_in_the_end(self, element):
        if self.head is None:
            new_node = self.Node(element)
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = self.Node(element)
        n.next = new_node
        new_node.previous = n

    def incertion_sort(self):
        tmp = self.head
        while tmp is not None:
            tmp1 = tmp.next
            while tmp1 is not None:
                if tmp1.element.experience < tmp.element.experience:
                    tmp1.element.experience, tmp.element.experience = tmp.element.experience, \
                                                                              tmp1.element.experience
                tmp1 = tmp1.next
            tmp = tmp.next

    def print_by_surname(self, surname: str) -> None:
        node = self.head
        while node is not None:
            if node.element.surname == surname:
                print(node.element)
            node = node.next

    def __iter__(self):
        node = self.head

        while node:
            yield node.element
            node = node.next

