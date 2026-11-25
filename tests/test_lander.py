"""
ORBITLINK - Lander Unit Tests

Tests sensor generation, telemetry packet creation,
and priority assignment.
"""

import unittest

from simulator.lander import Lander
from simulator.packet import Priority


class TestLander(unittest.TestCase):

    def setUp(self):
        self.lander = Lander()

    def test_sensor_readings_are_generated(self):
        readings = self.lander.read_sensors()

        self.assertEqual(len(readings), 5)

    def test_sensor_values_are_within_valid_ranges(self):
        readings = self.lander.read_sensors()

        self.assertGreaterEqual(readings["battery_voltage"], 6.0)
        self.assertLessEqual(readings["battery_voltage"], 8.4)

        self.assertGreaterEqual(readings["temperature"], -50.0)
        self.assertLessEqual(readings["temperature"], 20.0)

        self.assertGreaterEqual(readings["oxygen_level"], 0.0)
        self.assertLessEqual(readings["oxygen_level"], 100.0)

        self.assertGreaterEqual(readings["pressure"], 400.0)
        self.assertLessEqual(readings["pressure"], 900.0)

        self.assertGreaterEqual(readings["vibration"], 0.0)
        self.assertLessEqual(readings["vibration"], 5.0)

    def test_five_packets_are_generated(self):
        packets = self.lander.generate_packets(100)

        self.assertEqual(len(packets), 5)

    def test_packets_have_correct_source(self):
        packets = self.lander.generate_packets(100)

        for packet in packets:
            self.assertEqual(packet.source, "LANDER")

    def test_packets_have_correct_timestamp(self):
        mission_time = 250.5

        packets = self.lander.generate_packets(mission_time)

        for packet in packets:
            self.assertEqual(packet.timestamp, mission_time)

    def test_low_battery_triggers_emergency_priority(self):
        priority = self.lander.get_priority(
            "battery_voltage", 6.2
        )

        self.assertEqual(priority, Priority.EMERGENCY)

    def test_low_oxygen_triggers_emergency_priority(self):
        priority = self.lander.get_priority(
            "oxygen_level", 10.0
        )

        self.assertEqual(priority, Priority.EMERGENCY)

    def test_normal_battery_has_normal_priority(self):
        priority = self.lander.get_priority(
            "battery_voltage", 7.5
        )

        self.assertEqual(priority, Priority.NORMAL)

    def test_high_vibration_triggers_high_priority(self):
        priority = self.lander.get_priority(
            "vibration", 4.5
        )

        self.assertEqual(priority, Priority.HIGH)

    def test_high_temperature_triggers_high_priority(self):
        priority = self.lander.get_priority(
            "temperature", 18.0
        )

        self.assertEqual(priority, Priority.HIGH)


if __name__ == "__main__":
    unittest.main()