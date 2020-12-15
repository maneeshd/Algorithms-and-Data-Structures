from singly_linked_list import SinglyLinkedList


def merge_sorted_linked_lists(
    l1: SinglyLinkedList, l2: SinglyLinkedList
) -> SinglyLinkedList:
    if not l1.head and l2.head:
        return l2
    elif not l2.head:
        return l1

    head = None
    cur = None
    node = None
    ptr1 = l1.head
    ptr2 = l2.head

    while ptr1 and ptr2:
        if ptr1.data <= ptr2.data:
            node = ptr1
            ptr1 = ptr1.next
        else:
            node = ptr2
            ptr2 = ptr2.next

        if head is None:
            cur = node
            cur.next = None
            head = cur
        else:
            cur.next = node
            cur = cur.next

    if ptr1:
        cur.next = ptr1
    if ptr2:
        cur.next = ptr2

    return SinglyLinkedList(head)


if __name__ == "__main__":
    L1 = SinglyLinkedList()
    for x in range(10, -1, -1):
        L1.prepend(x)

    L2 = SinglyLinkedList()
    for x in range(15, 0, -2):
        L2.prepend(x)

    print(f"Linked List 1     : {L1}")
    print(f"Linked List 2     : {L2}")

    RES = merge_sorted_linked_lists(L1, L2)

    print(f"\nMerged Linked List: {RES}")
