from linked_lists.data_structures import LinkedList
from linked_lists.insert_element import insert_sorted


def test_linked_list():
    ll = LinkedList()
    ll.head.value = 0
    ll.append(1)
    ll.append(2)
    assert ll.to_list() == [0, 1, 2]

def test_insert_element():
    l = LinkedList((1,2,4))
    insert_sorted(l.head, 3)
    assert [1, 2, 3, 4] == l.to_list
