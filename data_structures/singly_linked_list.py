"""
Author: Maneesh D <maneeshd77@gmail.com>

Implementation of Singly-Linked-List
"""
from sys import getsizeof
from typing import Any, Tuple, TypeVar


typeLinkedList = TypeVar("SinglyLinkedList")
typeNode = TypeVar("Node")


class Node:
    """
    Node in a Singly-Linked-List.
    """

    __name__ = "Node"

    def __init__(self, data, next=None):
        """
        Create a Node
        """
        self.data = data
        self.next = next

    def __str__(self):
        """
        String representation of the Node object.
        """
        return "[{0}]".format(self.data)

    def __repr__(self):
        """
        Printable representation of the Node object.
        """
        return "%s(%r, %r)" % (self.__name__, self.data, self.next)

    def __len__(self):
        """
        Length of a Node. Always returns 1
        """
        return 1

    def __sizeof__(self):
        """
        Overriding to get the size of node data
        """
        return getsizeof(self.data)

    def __eq__(self, other):
        """
        Overriding the `euqals` operation
        """
        return self.data == other.data

    def __ge__(self, other):
        """
        Overriding the `greater than or euqals` operation
        """
        return self.data >= other.data

    def __le__(self, other):
        """
        Overriding the `lesser than or euqals` operation
        """
        return self.data <= other.data

    def __lt__(self, other):
        """
        Overriding the `lesser than` operation
        """
        return self.data < other.data

    def __gt__(self, other):
        """
        Overriding the `greater than` operation
        """
        return self.data > other.data

    def get_memory_footprint(self):
        """
        Total amount of memory used by a Node in Bytes
        """
        return self.__sizeof__() + getsizeof(self)


class SinglyLinkedList:
    """
    Singly-Linked-List
    """

    __name__ = "SinglyLinkedList"

    def __init__(self, head: Node = None) -> None:
        """
        Create a Singly-Linked-List
        O(1)
        """
        self.head = head
        self.__desc = False

    def is_circular(self) -> bool:
        """Checks if the linked list has a cycle
        O(n)
        """
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def __str__(self) -> str:
        """
        String representation of linked list.
        O(n)
        """
        nodes = list()
        if self.head:
            cur_node = self.head
            fast = self.head
            while cur_node:
                nodes.append(str(cur_node))
                cur_node = cur_node.next
                if fast and fast.next:
                    fast = fast.next.next
                    if cur_node is fast:
                        print(
                            "[CRITICAL] ! Cycle detected in the linked list. Stopping iteration. !"
                        )
                        nodes.append(str(cur_node))
                        break
            return "HEAD => {0}".format(" -> ".join(nodes))
        else:
            return "HEAD => None"

    def __repr__(self) -> str:
        """
        Printable representation of the SinglyLinkedList object.
        O(1)
        """
        return "%s(%r)" % (self.__name__, self.head)

    def __len__(self) -> int:
        """
        Number of nodes in the linked list
        O(n)
        """
        num_of_nodes = 0
        cur_node = self.head
        while cur_node:
            num_of_nodes += 1
            cur_node = cur_node.next
        return num_of_nodes

    def __sizeof__(self) -> float:
        """
        Total size of the linked list
        O(n)
        """
        size = 0
        cur_node = self.head
        while cur_node:
            size += cur_node.get_memory_footprint()
            cur_node = cur_node.next
        return size

    def prepend(self, data: Any) -> None:
        """
        Insert data at the begining of the linked list.
        O(1)
        """
        if not self.head:
            if isinstance(data, Node):
                self.head = data
            else:
                self.head = Node(data)
        else:
            if isinstance(data, Node):
                data.next = self.head
                self.head = data
            else:
                self.head = Node(data, next=self.head)

    def append(self, data: Any) -> None:
        """
        Insert data at the end of the linked list.
        O(n)
        """
        if not self.head:
            if isinstance(data, Node):
                self.head = data
            else:
                self.head = Node(data)
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            if isinstance(data, Node):
                cur_node.next = data
            else:
                cur_node.next = Node(data)

    def insert_before(self, node: Node, data: Any) -> None:
        """
        Insert data before the given node
        O(n)
        """
        if not self.head:
            print("! LinkedList is empty. Prepending as the first node. !")
            if isinstance(data, Node):
                self.head = data
            else:
                self.head = Node(data)
        else:
            prev_node = None
            cur_node = self.head
            while cur_node:
                if cur_node is node:
                    break
                prev_node = cur_node
                cur_node = cur_node.next
            if cur_node:
                if prev_node:
                    if isinstance(data, Node):
                        data.next = cur_node
                        prev_node.next = data
                    else:
                        prev_node.next = Node(data, next=cur_node)
                else:
                    # It is the firt node
                    if isinstance(data, Node):
                        data.next = self.head
                        self.head = data
                    else:
                        self.head = Node(data, next=self.head)
            else:
                print("! Did not find the node to insert !")

    def insert_after(self, node: Node, data: Any) -> None:
        """
        Insert data after the given node
        O(n)
        """
        if not self.head:
            print("! LinkedList is empty. Appending as the first node. !")
            if isinstance(data, Node):
                self.head = data
            else:
                self.head = Node(data)
        else:
            cur_node = self.head
            while cur_node:
                if cur_node is node:
                    break
                cur_node = cur_node.next
            if cur_node:
                next_node = cur_node.next
                if next_node:
                    if isinstance(data, Node):
                        data.next = next_node
                        cur_node.next = data
                    else:
                        cur_node.next = Node(data, next=next_node)
                else:
                    # First or the last node
                    if isinstance(data, Node):
                        cur_node.next = data
                    else:
                        cur_node.next = Node(data)
            else:
                print("! Did not find the node to insert !")

    def __getitem__(self, search_key: Any) -> Node:
        """
        Search for the first occurance of a node with `data` matching `search_key`.
        Returns the `Node` if found else returns `None`
        Ex: linked_list[1]
        O(n)
        """
        cur_node = self.head
        if isinstance(search_key, Node):
            while cur_node and cur_node is not search_key:
                cur_node = cur_node.next
        else:
            while cur_node and cur_node.data != search_key:
                cur_node = cur_node.next
        # cur will be None if it hits the end of list or list is empty
        return cur_node

    def search(self, search_key: Any) -> Node:
        """
        Alias/Wrapper for __getitem__
        """
        return self.__getitem__(search_key)

    def remove(self, search_key: Any) -> str:
        """
        Remove for the first occurance of a node with `data` matching `search_key`.
        O(n)
        """
        cur_node = self.head
        prev = None
        if isinstance(search_key, Node):
            while cur_node and cur_node is not search_key:
                prev = cur_node
                cur_node = cur_node.next
        else:
            while cur_node and cur_node.data != search_key:
                prev = cur_node
                cur_node = cur_node.next
        if prev is None and cur_node:
            self.head = cur_node.next
            return "Node: {0} - removed.".format(cur_node)
        elif cur_node:
            prev.next = cur_node.next
            cur_node.next = None
            return "Node: {0} - removed.".format(cur_node)
        else:
            return "! Did not find the node to be removed !"

    def reverse(self) -> None:
        """
        Reverse the linked list
        O(n)
        """
        cur_node = self.head
        prev_node = None
        next_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def get_memory_footprint(self) -> float:
        """
        Amount of memory used by the linked list in Bytes
        O(n) + O(1)
        """
        return self.__sizeof__() + getsizeof(self)

    def __split_in_half(self, head: Node) -> Tuple[typeNode, typeNode]:
        """
        Split the linked list in half using front-back splitting
        """
        if head is None or head.next is None:
            return head, None

        left_half = None
        right_half = None

        slow = head
        fast = head.next

        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next

        left_half = head
        right_half = slow.next
        slow.next = None

        return left_half, right_half

    def __merge(self, left_half: typeNode, right_half: typeNode) -> typeNode:
        """
        Merge the divided linked list
        """
        if left_half is None and right_half is not None:
            return right_half
        elif right_half is None:
            return left_half

        merged = None
        cur = None
        node = None
        l_ptr = left_half
        r_ptr = right_half

        while l_ptr and r_ptr:
            if self.__desc:
                if l_ptr.data >= r_ptr.data:
                    node = l_ptr
                    l_ptr = l_ptr.next
                else:
                    node = r_ptr
                    r_ptr = r_ptr.next
            else:
                if l_ptr.data <= r_ptr.data:
                    node = l_ptr
                    l_ptr = l_ptr.next
                else:
                    node = r_ptr
                    r_ptr = r_ptr.next

            if not cur:
                cur = node
                cur.next = None
                merged = cur
            else:
                cur.next = node
                cur = cur.next

        if l_ptr:
            cur.next = l_ptr

        if r_ptr:
            cur.next = r_ptr

        return merged

    def __merge_sort(self, head: typeNode) -> typeNode:
        """
        Sorts the linked list using MergeSort
        """
        if head is None or head.next is None:
            return head

        left_half, right_half = self.__split_in_half(head)

        left_merged = self.__merge_sort(left_half)
        right_merged = self.__merge_sort(right_half)

        # Final merge before returning
        return self.__merge(left_merged, right_merged)

    def sort(self, desc: bool = False) -> None:
        """
        Sorts the Linked List using MergeSort
        """
        if desc:
            self.__desc = True
        self.head = self.__merge_sort(self.head)


if __name__ == "__main__":
    print("Singly-Linked-List")
    print("------------------")

    # Create the linked list
    print("\nCreating an empty linked list...")
    linked_list = SinglyLinkedList()
    print("Linked List:", linked_list)

    """
    # Add at the back of the linked list
    print("\nAdding data=1 at the back of the linked list...")
    linked_list.append(1)
    print(linked_list)

    # Add at the begining of the linked list
    print("\nAdding data=2 at the begining of the linked list...")
    linked_list.prepend(2)
    print(linked_list)
    """
    print("\nInserting numbers [10, 99] in descending order...")
    for x in range(10, 100):
        linked_list.prepend(x)

    print("Linked List:", linked_list)

    # Length of the linked list
    print("\nNumber of nodes in the linked list:", len(linked_list))

    # Size of the linked list
    print(
        "\nMemory footprint of the linked list:",
        linked_list.get_memory_footprint(),
        "Bytes",
    )
    """
    # Search the linked list
    print("\nSearching for data=1 in the linked list...")
    print(linked_list.search(1))

    # Search the linked list
    print(
        "\nSearching for data=1 in the linked list using getitem i.e. linked_list[1]..."
    )
    print(linked_list[1])

    # Reverse the linked list
    print("\nReversing the linked list...")
    linked_list.reverse()
    print(linked_list)

    # Remove nodes from the list
    print("\nRemoving data=2 from the linked list...")
    print(linked_list.remove(2))
    print("\nRemoving data=1 from the linked list...")
    print(linked_list.remove(1))
    print("\n[NEGATIVE] Removing data=0 from the linked list...")
    print(linked_list.remove(0))

    print("\nFinal state of the linked list...")
    print(linked_list)
    """
    print("\nSorting...")
    linked_list.sort()
    print("Linked List:", linked_list)
