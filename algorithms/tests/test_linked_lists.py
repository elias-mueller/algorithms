from algorithms.linked_lists.data_structures import LinkedList
from algorithms.linked_lists.insert_element import insert_sorted


def test_linked_list():
    ll = LinkedList()
    ll.head.value = 0
    ll.append(1)
    ll.append(2)
    assert ll.aslist() == [0, 1, 2]


def test_insert_element():
    l = LinkedList()
    insert_sorted(l.head, 1)
    assert l.aslist() == [1]

    l.append(2)
    l.append(4)
    insert_sorted(l.head, 3)
    assert l.aslist() == [1, 2, 3, 4]

    insert_sorted(l.head, 5)
    assert l.aslist() == [1, 2, 3, 4, 5]
