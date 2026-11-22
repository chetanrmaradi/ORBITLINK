import unittest

from simulator.packet import (
    Packet,
    Priority,
    PacketStatus,
    create_packet
)


class TestPacketSystem(unittest.TestCase):

    def test_packet_creation(self):
        packet = create_packet(
            source="LANDER",
            priority=Priority.NORMAL,
            data_type="TEMPERATURE",
            timestamp=10,
            payload="-35 C"
        )

        self.assertIsInstance(packet, Packet)

    def test_packet_id_is_generated(self):
        packet = create_packet(
            "LANDER",
            Priority.NORMAL,
            "TEMPERATURE",
            10,
            "-35 C"
        )

        self.assertTrue(packet.packet_id.startswith("ORB-"))

    def test_unique_packet_ids(self):
        packet1 = create_packet(
            "LANDER",
            Priority.NORMAL,
            "TEMPERATURE",
            10,
            "-35 C"
        )

        packet2 = create_packet(
            "LANDER",
            Priority.NORMAL,
            "PRESSURE",
            11,
            "600 Pa"
        )

        self.assertNotEqual(packet1.packet_id, packet2.packet_id)

    def test_emergency_priority(self):
        packet = create_packet(
            "LANDER",
            Priority.EMERGENCY,
            "BATTERY_ALERT",
            12,
            "Battery critically low"
        )

        self.assertEqual(packet.priority, Priority.EMERGENCY)

    def test_initial_packet_status(self):
        packet = create_packet(
            "LANDER",
            Priority.NORMAL,
            "TEMPERATURE",
            10,
            "-35 C"
        )

        self.assertEqual(packet.status, PacketStatus.CREATED)


if __name__ == "__main__":
    unittest.main()