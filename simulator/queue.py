"""
ORBITLINK - Priority Packet Queue

Stores packets and selects the next packet
based on priority and arrival order.
"""

import heapq


class PacketQueue:

    def __init__(self):
        self._queue = []
        self._counter = 0

    def enqueue(self, packet):
        """
        Add a packet to the queue.

        Lower priority number means higher importance.
        FIFO is maintained for equal priorities.
        """

        packet.status = "QUEUED"

        heapq.heappush(
            self._queue,
            (
                int(packet.priority),
                self._counter,
                packet
            )
        )

        self._counter += 1

    def dequeue(self):
        """
        Remove and return the highest-priority packet.
        """

        if self.is_empty():
            return None

        _, _, packet = heapq.heappop(self._queue)

        return packet

    def peek(self):
        """
        Return the next packet without removing it.
        """

        if self.is_empty():
            return None

        return self._queue[0][2]

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)