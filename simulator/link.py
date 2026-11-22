
"""
ORBITLINK - Communication Link Simulator

Simulates periodic communication windows between
a planetary lander and an orbiting relay.
"""


class CommunicationLink:
    def __init__(self, cycle_duration=20, window_duration=8):
        self.cycle_duration = cycle_duration
        self.window_duration = window_duration

    def is_available(self, mission_time):
        """
        Return True if communication is available
        at the given mission time.
        """

        position_in_cycle = mission_time % self.cycle_duration

        return position_in_cycle < self.window_duration

    def get_status(self, mission_time):
        if self.is_available(mission_time):
            return "ONLINE"
        return "OFFLINE"


if __name__ == "__main__":
    link = CommunicationLink()

    print("=== ORBITLINK Communication Link Simulation ===")
    print("Lander <----> Orbiter")
    print()

    for mission_time in range(40):
        status = link.get_status(mission_time)

        print(
            f"Mission Time: {mission_time:02d}s | "
            f"Link Status: {status}"
        )
