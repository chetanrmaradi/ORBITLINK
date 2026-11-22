import unittest

from simulator.packet import Priority, create_packet
from simulator.queue import PacketQueue


class TestPacketQueue(unittest.TestCase):

    def setUp(self):
        self.queue = PacketQueue()

    def create_test_packet(self, priority, data_type):
        return create_packet(
            source="LANDER",
            priority=priority,
            data_type=data_type,
            timestamp=0,
            payload="Test data"
        )

    def test_empty_queue(self):
        self.assertTrue(self.queue.is_empty())

    def test_enqueue_increases_size(self):
        packet = self.create_test_packet(
            Priority.NORMAL,
            "TEMPERATURE"
        )

        self.queue.enqueue(packet)

        self.assertEqual(self.queue.size(), 1)

    def test_dequeue_returns_packet(self):
        packet = self.create_test_packet(
            Priority.NORMAL,
            "TEMPERATURE"
        )

        self.queue.enqueue(packet)

        result = self.queue.dequeue()

        self.assertEqual(result.packet_id, packet.packet_id)

    def test_emergency_packet_first(self):
        bulk = self.create_test_packet(
            Priority.BULK,
            "IMAGE"
        )

        emergency = self.create_test_packet(
            Priority.EMERGENCY,
            "BATTERY_ALERT"
        )

        normal = self.create_test_packet(
            Priority.NORMAL,
            "TEMPERATURE"
        )

        self.queue.enqueue(bulk)
        self.queue.enqueue(normal)
        self.queue.enqueue(emergency)

        result = self.queue.dequeue()

        self.assertEqual(
            result.priority,
            Priority.EMERGENCY
        )

    def test_priority_order(self):
        packets = [
            self.create_test_packet(Priority.BULK, "IMAGE"),
            self.create_test_packet(Priority.NORMAL, "TEMP"),
            self.create_test_packet(Priority.HIGH, "VIBRATION"),
            self.create_test_packet(Priority.EMERGENCY, "ALERT"),
        ]

        for packet in packets:
            self.queue.enqueue(packet)

        priorities = []

        while not self.queue.is_empty():
            priorities.append(self.queue.dequeue().priority)

        self.assertEqual(
            priorities,
            [
                Priority.EMERGENCY,
                Priority.HIGH,
                Priority.NORMAL,
                Priority.BULK,
            ]
        )

    def test_fifo_for_equal_priorities(self):
        first = self.create_test_packet(
            Priority.EMERGENCY,
            "FIRST_ALERT"
        )

        second = self.create_test_packet(
            Priority.EMERGENCY,
            "SECOND_ALERT"
        )

        self.queue.enqueue(first)
        self.queue.enqueue(second)

        self.assertEqual(
            self.queue.dequeue().packet_id,
            first.packet_id
        )

        self.assertEqual(
            self.queue.dequeue().packet_id,
            second.packet_id
        )

    def test_peek_does_not_remove_packet(self):
        packet = self.create_test_packet(
            Priority.HIGH,
            "VIBRATION"
        )

        self.queue.enqueue(packet)

        result = self.queue.peek()

        self.assertEqual(result.packet_id, packet.packet_id)
        self.assertEqual(self.queue.size(), 1)

    def test_dequeue_empty_queue(self):
        self.assertIsNone(self.queue.dequeue())

    def test_packet_status_changes_to_queued(self):
        packet = self.create_test_packet(
            Priority.NORMAL,
            "TEMPERATURE"
        )

        self.queue.enqueue(packet)

        self.assertEqual(packet.status, "QUEUED")


if __name__ == "__main__":
    unittest.main()