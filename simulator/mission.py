
"""
ORBITLINK - Mission Controller

Coordinates the Lander, packet queue,
and communication link.
"""

from simulator.lander import Lander
from simulator.queue import PacketQueue
from simulator.link import CommunicationLink


class MissionSimulation:

    def __init__(self):

        # Initialize spacecraft systems
        self.lander = Lander()

        # Initialize packet storage
        self.packet_queue = PacketQueue()

        # Initialize communication link
        self.link = CommunicationLink()

        # Mission clock
        self.mission_time = 0

    def generate_telemetry(self):
        """
        Generate lander telemetry packets
        and add them to the priority queue.
        """

        packets = self.lander.generate_packets(
            self.mission_time
        )

        for packet in packets:
            self.packet_queue.enqueue(packet)

        return packets

    def display_queue(self):
        """
        Display queued packets in transmission order.
        """

        ordered_packets = (
            self.packet_queue.get_ordered_packets()
        )

        print("\n=== ORBITLINK PACKET QUEUE ===")

        for packet in ordered_packets:
            print(
                f"P{packet.priority} | "
                f"{packet.data_type:20} | "
                f"{packet.payload:10} | "
                f"{packet.status}"
            )

        print(f"\nTotal queued packets: {len(ordered_packets)}")
