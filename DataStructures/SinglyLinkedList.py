"""
Author: Maneesh D <maneeshd77@gmail.com>

Implementation of Singly-Linked-List
"""
from __future__ import print_function
from sys import getsizeof


class Node:
    """
    Node in a Singly-Linked-List.
    """
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
        return "%s(%r, %r)" % (self.__class__, self.data, self.next)

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
    def __init__(self, head=None):
        """
        Create a Singly-Linked-List
        O(1)
        """
        self.head = head

    def __str__(self):
        """
        String representation of linked list.
        O(n)
        """
        nodes = list()
        if self.head:
            cur_node = self.head
            while cur_node:
                nodes.append(str(cur_node))
                cur_node = cur_node.next
            return "HEAD -> {0}".format(" -> ".join(nodes))
        else:
            return "HEAD -> None"

    def __repr__(self):
        """
        Printable representation of the Node object.
        O(1)
        """
        return "%s(%r)" % (self.__class__, self.head)

    def __len__(self):
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

    def __sizeof__(self):
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

    def prepend(self, data):
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

    def append(self, data):
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

    def insert_before(self, node, data):
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

    def insert_after(self, node, data):
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

    def __getitem__(self, search_key):
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

    def search(self, search_key):
        """
        Alias/Wrapper for __getitem__
        """
        return self.__getitem__(search_key)

    def remove(self, search_key):
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

    def reverse(self):
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

    def get_memory_footprint(self):
        """
        Amount of memory used by the linked list in Bytes
        O(n) + O(1)
        """
        return self.__sizeof__() + getsizeof(self)

    def __split_linked_list(self, head):
        """
        Split the linked list using front-back splitting
        """
        if head is None or head.next is None:
            left_half = head
            right_half = None
        else:
            slow = head
            fast = head.next
            while fast:
                fast = fast.next
                if fast:
                    slow = slow.next
                    fast = fast.next
            left_half = head
            right_half = slow.next
        return left_half, right_half

    def __merge(self, left_half, right_half, reverse=False):
        """
        Merge the divided linked list
        """
        if left_half is None:
            return right_half
        if right_half is None:
            return left_half
        cur = None
        head = None
        while left_half and right_half:
            if left_half.data <= right_half.data:
                node = left_half
                left_half = left_half.next
            else:
                node = right_half
                right_half = right_half.next
            if not head:
                head = node
                cur = node
            else:
                cur.next = node
                cur = cur.next
        cur.next = left_half or right_half
        return head

    def __merge_sort(self, head, desc=False):
        """
        Sorts the linked list using MergeSort
        """
        if head is None or head.next is None:
            return
        left_half, right_half = self.__split_linked_list(head)
        self.__merge_sort(left_half, desc)
        self.__merge_sort(right_half, desc)
        new_head = self.__merge(left_half, right_half, desc)
        return new_head

    def sort(self, desc=False):
        """
        Sort the Linked List
        """
        self.head = self.__merge_sort(self.head, desc)


if __name__ == "__main__":
    print("Singly-Linked-List")
    print("------------------")

    # Create the linked list
    print("\nCreating an empty linked list...")
    linked_list = SinglyLinkedList()
    print(linked_list)
    print("")

    # Add at the back of the linked list
    print("\nAdding data=1 at the back of the linked list...")
    linked_list.append(1)
    print(linked_list)

    # Add at the begining of the linked list
    print("\nAdding data=2 at the begining of the linked list...")
    linked_list.prepend(2)
    print(linked_list)

    # Length of the linked list
    print("\nNumber of nodes in the linked list:", len(linked_list))

    # Size of the linked list
    print("\nMemory footprint of the linked list:", linked_list.get_memory_footprint(), "Bytes")

    # Search the linked list
    print("\nSearching for data=1 in the linked list...")
    print(linked_list.search(1))

    # Search the linked list
    print("\nSearching for data=1 in the linked list using getitem i.e. linked_list[1]...")
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
