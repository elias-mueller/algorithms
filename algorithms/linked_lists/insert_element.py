from algorithms.linked_lists.data_structures import LinkedList


def insert_sorted(head, val):
    if not head.value:
        head.value = val
        return
    new_elem = LinkedList.Element(val)
    e = head
    while e:
        if e.next:
            if e.next.value >= val:
                new_elem.next = e.next
                e.next = new_elem
                break
        else:
            e.next = new_elem
            break
        e = e.next
