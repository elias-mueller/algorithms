from linked_lists.data_structures import LinkedList


def insert_sorted(head, val):
    e = head
    while e.next:
        if e.value <= val:
            new_elem = LinkedList.Element(val)
            new_elem.next = e.next
            e.next = new_elem
