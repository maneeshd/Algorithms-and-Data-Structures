from SinglyLinkedList import SinglyLinkedList, Node


def odd_even(l: SinglyLinkedList) -> SinglyLinkedList:
    """Groups all nodes at odd positions in the linked list to the begining of
    the linked list and all nodes at even positions to the end of the linked
    list.

    :param l: A singly linked list class object
    :type l: SinglyLinkedList

    :return: A singly linked list class object
    :rtype: SinglyLinkedList
    """
    if l.head is None:
        return l
    odd = l.head
    even = l.head.next
    even_first = even
    count = 1
    while True:
        # print(f"Iteration-{count} :: {l}\n")
        if not odd or not even or not even.next:
            odd.next = even_first
            # print(f"Iteration-{count}-Null-Break :: {l}\n")
            break
        odd.next = even.next
        odd = even.next
        if odd.next is None:
            even.next = None
            odd.next = even_first
            # print(f"Iteration-{count}-Last-Node-Break :: {l}\n")
            break
        even.next = odd.next
        even = odd.next
        count += 1
    return l


def recur_reverse(node: Node) -> Node:
    """Reverse a given linked list in-place.

    :param l: A singly linked list class object
    :type l: SinglyLinkedList
    """
    if node is None or node.next is None:
        return node
    new_node = recur_reverse(node.next)
    node.next.next = node
    node.next = None
    return new_node


def iter_reverse(l: SinglyLinkedList) -> None:
    """Reverse a given linked list in-place.

    :param l: A singly linked list class object
    :type l: SinglyLinkedList
    """
    pre = None
    cur = l.head
    nxt = None
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    l.head = pre


def find_median_node(l: SinglyLinkedList) -> Node:
    """Find the median/middle of the linked list.

    :param l: A singly linked list class object
    :type l: SinglyLinkedList

    :return: Median/Middle Node
    :rtype: Node
    """
    slow = l.head
    fast = l.head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def is_circular(l: SinglyLinkedList) -> bool:
    """Checks if the given linked list is circular.

    ***** Using Floyd's Cycle Finding ALgorithm *****

    :param l: A singly linked list class object
    :type l: SinglyLinkedList list class object
    :type l: SinglyLinkedList

    :return: A singly linked list class object
    :rtype: SinglyLinkedList
    """
    if l.head is None:
        return True

    slow = l.head
    fast = l.head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


def tester(s1: str, s2: str) -> bool:
    return "PASS" if s1 == s2 else "FAIL"


if __name__ == "__main__":
    # Empty
    l0 = SinglyLinkedList()

    # Odd number of nodes
    l1 = SinglyLinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(4)
    l1.append(5)

    # Even number of nodes
    l2 = SinglyLinkedList()
    l2.append(1)
    l2.append(2)
    l2.append(3)
    l2.append(4)

    # One node
    l3 = SinglyLinkedList()
    l3.append(1)

    # Two nodes
    l4 = SinglyLinkedList()
    l4.append(1)
    l4.append(2)

    # Circular number of nodes
    l5 = SinglyLinkedList()
    l5.append(1)
    l5.append(2)
    l5.append(3)
    l5.head.next.next = l5.head.next

    # Ascending order of nodes
    l6 = SinglyLinkedList()
    l6.append(1)
    l6.append(2)
    l6.append(3)
    l6.append(4)
    l6.append(5)

    try:
        odd_even(l0)
        test_0 = tester("HEAD -> None", str(l0))
        odd_even(l1)
        test_1 = tester("HEAD -> [1] -> [3] -> [5] -> [2] -> [4]", str(l1))
        odd_even(l2)
        test_2 = tester("HEAD -> [1] -> [3] -> [2] -> [4]", str(l2))
        odd_even(l3)
        test_3 = tester("HEAD -> [1]", str(l3))
        odd_even(l4)
        test_4 = tester("HEAD -> [1] -> [2]", str(l4))

        print("")
        print("-" * 32)
        print("Odd-Even-Rearrange Testcases")
        print("-" * 32)
        print(f"Testcase-1 :: {test_0}")
        print(f"Testcase-2 :: {test_1}")
        print(f"Testcase-3 :: {test_2}")
        print(f"Testcase-4 :: {test_3}")
        print(f"Testcase-5 :: {test_4}")
        print("-" * 32)

        print("")
        print("-" * 32)
        print("Is-Circular? Testcases")
        print("-" * 32)
        test_0 = "PASS" if is_circular(l0) else "FAIL"    # Circular
        test_1 = "FAIL" if is_circular(l1) else "PASS"    # Non-circular
        test_2 = "PASS" if is_circular(l5) else "FAIL"    # Circular
        print(f"Testcase-1 :: {test_0}")
        print(f"Testcase-2 :: {test_1}")
        print(f"Testcase-3 :: {test_2}")
        print("-" * 32)

        print(f"\nReverse of {l6} is ", end="")
        iter_reverse(l6)
        print(l6)

        print(f"\nMedian of {l6} is {find_median_node(l6)}")

        print(f"\nReverse of {l6} is ", end="")
        l6.head = recur_reverse(l6.head)
        print(l6)
    except Exception as exp:
        print(exp)
    finally:
        del l0, l1, l2, l3, l4, l5
