from __future__ import print_function
from sys import getsizeof
from random import randint


class Queue:
    """
    Queue
    """
    def __init__(self, max_size=1000000):
        """
        Creates an empty single-ended Queue
        :param max_size: Maximum allowed size of the queue.
        """
        self.max_size = int(max_size)
        self.queue = list()
        self.size = 0

    def __str__(self):
        """
        String representation of the Queue object.
        """
        return "Queue: {0}\nSize: {1}".format(self.queue, self.size)

    def __repr__(self):
        """
        Printable representation of the Queue object.
        """
        return "%s(%r)" % (self.__class__, self.max_size)

    def __len__(self):
        """
        Number of items present in the Queue.
        """
        return self.size

    def __sizeof__(self):
        """
        Overriding to get the total size of Queue data
        """
        size = 0
        for ele in self.queue:
            size += getsizeof(ele)
        return size

    def enqueue(self, data):
        """
        Insert an item into Queue

        :param data: Data to be queued
        """
        if self.size >= self.max_size:
            print("[QueueOverflow] Lost Data: {0} !".format(data))
        else:
            self.queue.append(data)
            self.size += 1

    def dequeue(self):
        """
        Remove an item from the Queue

        :returns: The removed item from Queue
        """
        if self.size < 1:
            print("[QueueUnderflow] Cannot dequeue !")
        else:
            data = self.queue.pop(0)
            self.size -= 1
            return data

    def get_memory_footprint(self):
        """
        Total amount of memory used by a Queue in Bytes
        """
        return self.__sizeof__() + getsizeof(self)


if __name__ == "__main__":
    print("Queue")
    print("-----")

    queue = Queue(max_size=10)
    repr(queue)
    print(queue)

    print("\nEnqueueing 10 random numbers")
    for _ in range(10):
        queue.enqueue(randint(1, 1000000))
    print(queue)

    print("\nTrying to eneque when queue is full:")
    queue.enqueue("random")

    print("\nMemory footprint of queue: {0} Bytes".format(queue.get_memory_footprint()))

    print("\nDequeuing 4 items...")
    print("\tdequeued:", queue.dequeue())
    print("\tdequeued:", queue.dequeue())
    print("\tdequeued:", queue.dequeue())
    print("\tdequeued:", queue.dequeue())

    print("\nDequeuing and emptying queue...")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print("\nNow now, you cannot dequeue from an empty queue...")
    print(queue.dequeue())

    print("\nFinal state of queue:")
    print(queue)
