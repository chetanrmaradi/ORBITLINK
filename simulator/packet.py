"""
ORBITLINK - Packet System

Defines the data packets transmitted
between the Lander and Orbiter.
"""

from dataclasses import dataclass
from enum import IntEnum
from uuid import uuid4


class Priority(IntEnum):
    EMERGENCY = 0
    HIGH = 1
    NORMAL = 2
    BULK = 3


class PacketStatus:
    CREATED = "CREATED"
    QUEUED = "QUEUED"
    SENT = "SENT"
    ACKNOWLEDGED = "ACKNOWLEDGED"


@dataclass
class Packet:
    packet_id: str
    source: str
    priority: Priority
    data_type: str
    timestamp: float
    payload: str
    status: str = PacketStatus.CREATED


def create_packet(
    source,
    priority,
    data_type,
    timestamp,
    payload
):
    """
    Create a new ORBITLINK data packet.
    """

    packet_id = f"ORB-{uuid4().hex[:8].upper()}"

    return Packet(
        packet_id=packet_id,
        source=source,
        priority=priority,
        data_type=data_type,
        timestamp=timestamp,
        payload=payload
    )


if __name__ == "__main__":

    packet = create_packet(
        source="LANDER",
        priority=Priority.EMERGENCY,
        data_type="BATTERY_ALERT",
        timestamp=125.5,
        payload="Battery critically low"
    )

    print("=== ORBITLINK PACKET ===")
    print(f"Packet ID : {packet.packet_id}")
    print(f"Source    : {packet.source}")
    print(f"Priority  : P{packet.priority}")
    print(f"Type      : {packet.data_type}")
    print(f"Time      : {packet.timestamp}")
    print(f"Payload   : {packet.payload}")
    print(f"Status    : {packet.status}")