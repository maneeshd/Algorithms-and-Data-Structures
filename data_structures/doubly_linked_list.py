"""
Author: Maneesh D <maneeshd77@gmail.com>

Doubly-Linked-List
"""
from __future__ import absolute_import
from sys import getsizeof


class Node:
    """
    Node in a Doubly-Linked-List
    """

    def __init__(self, data, left=None, right=None):
        """
        Create a Node
        """
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """
        String representation of the Node object.
        """
        return "[{0}]".format(self.data)

    def __repr__(self):
        """
        Printable representation of the Node object.
        """
        return "%s(%r, %r, %r)" % (self.__class__, self.data, self.left, self.right)

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


class DoublyLinkedList:
    """
    Doubly-Linked-List
    """

    def __init__(self, head=None, tail=None):
        """
        Create a Doubly-Linked-List
        """
        self.head = head
        self.tail = tail

    def __str__(self):
        """
        String representation of linked list.
        O(n)
        """
        nodes = list()
        if self.head and self.tail:
            cur_node = self.head
            while cur_node:
                nodes.append(str(cur_node))
                cur_node = cur_node.next
            return "HEAD <=> {0} <=> TAIL".format(" <=> ".join(nodes))
        else:
            return "HEAD <=> None <=> TAIL"

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

    def __getitem__(self, search_key):
        """
        Search for the first occurance of a node with `data` matching `search_key`.
        Returns the `Node` if found else returns `None`
        Ex: linked_list[1]
        O(n)
        """
        cur_node = self.head
        while cur_node and cur_node.data != search_key:
            cur_node = cur_node.next
        # cur will be None if it hits the end of list or list is empty
        return cur_node

    def prepend(self, data):
        """
        Insert data at the begining of the linked list.
        O(1)
        """
        pass

    def append(self, data):
        """
        Insert data at the end of the linked list.
        O(n)
        """
        pass

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
        pass

    def reverse(self):
        """
        Reverse the linked list
        O(n)
        """
        pass

    def get_memory_footprint(self):
        """
        Amount of memory used by the linked list in Bytes
        O(n) + O(1)
        """
        return self.__sizeof__() + getsizeof(self)


if __name__ == "__main__":
    print("Doubly-Linked-List")
    print("------------------")

    # Create the linked list
    print("\nCreating an empty linked list...")
    linked_list = DoublyLinkedList()
    print(linked_list)
    print("")
