"""
ORBITLINK - Lander Telemetry Generator

Simulates onboard sensors and converts readings
into communication packets.
"""

import random

from simulator.packet import Priority, create_packet


class Lander:

    def __init__(self):
        self.battery_voltage = 7.2
        self.temperature = -35.0
        self.oxygen_level = 78.0
        self.pressure = 600.0
        self.vibration = 0.2

    def read_sensors(self):
        """
        Generate simulated sensor readings.
        """

        self.battery_voltage = round(
            random.uniform(6.0, 8.4), 2
        )

        self.temperature = round(
            random.uniform(-50.0, 20.0), 2
        )

        self.oxygen_level = round(
            random.uniform(0.0, 100.0), 2
        )

        self.pressure = round(
            random.uniform(400.0, 900.0), 2
        )

        self.vibration = round(
            random.uniform(0.0, 5.0), 2
        )

        return {
            "battery_voltage": self.battery_voltage,
            "temperature": self.temperature,
            "oxygen_level": self.oxygen_level,
            "pressure": self.pressure,
            "vibration": self.vibration,
        }

    def generate_packets(self, mission_time):
        """
        Read sensors and generate telemetry packets.
        """

        readings = self.read_sensors()
        packets = []

        for sensor, value in readings.items():

            priority = self.get_priority(sensor, value)

            packet = create_packet(
                source="LANDER",
                priority=priority,
                data_type=sensor.upper(),
                timestamp=mission_time,
                payload=str(value)
            )

            packets.append(packet)

        return packets

    def get_priority(self, sensor, value):
        """
        Determine packet priority based on sensor condition.
        """

        if sensor == "battery_voltage" and value < 6.5:
            return Priority.EMERGENCY

        if sensor == "oxygen_level" and value < 20:
            return Priority.EMERGENCY

        if sensor == "temperature" and value > 15:
            return Priority.HIGH

        if sensor == "vibration" and value > 4.0:
            return Priority.HIGH

        return Priority.NORMAL


if __name__ == "__main__":

    lander = Lander()

    mission_time = 100

    packets = lander.generate_packets(mission_time)

    print("=== LANDER SENSOR DATA ===")

    for packet in packets:
        print(f"{packet.data_type.lower()}: {packet.payload}")

    print()
    print("=== GENERATED PACKETS ===")

    for packet in packets:
        print(
            f"{packet.data_type:20} | "
            f"P{packet.priority} | "
            f"{packet.payload}"
        )