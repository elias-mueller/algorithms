from typing import Iterable


class LinkedList:

    class Element:
        __slots__ = ('value', 'next')

        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self, it: Iterable = None):
        self.head = self.Element()
        if it:
            e = self.head
            for i in it:
                e.value = i
                e.next = LinkedList.Element()
                e = e.next

    def append(self, val):
        self.get_last().next = LinkedList.Element(val)

    def get_last(self):
        e = self.head
        while e.next:
            e = e.next
        return e

    def aslist(self):
        l = []
        e = self.head
        while e.next:
            l.append(e.value)
            e = e.next
        l.append(e.value)
        return l
