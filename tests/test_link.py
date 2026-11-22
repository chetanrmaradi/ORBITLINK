
import unittest

from simulator.link import CommunicationLink


class TestCommunicationLink(unittest.TestCase):

    def setUp(self):
        self.link = CommunicationLink(
            cycle_duration=20,
            window_duration=8
        )

    def test_link_online_at_start(self):
        self.assertTrue(self.link.is_available(0))

    def test_link_online_at_last_window_second(self):
        self.assertTrue(self.link.is_available(7))

    def test_link_offline_when_window_ends(self):
        self.assertFalse(self.link.is_available(8))

    def test_link_offline_before_next_cycle(self):
        self.assertFalse(self.link.is_available(19))

    def test_link_online_when_next_cycle_starts(self):
        self.assertTrue(self.link.is_available(20))

    def test_second_window_boundary(self):
        self.assertTrue(self.link.is_available(27))
        self.assertFalse(self.link.is_available(28))

    def test_schedule_repeats(self):
        self.assertTrue(self.link.is_available(40))

    def test_status_returns_online(self):
        self.assertEqual(self.link.get_status(0), "ONLINE")

    def test_status_returns_offline(self):
        self.assertEqual(self.link.get_status(8), "OFFLINE")


if __name__ == "__main__":
    unittest.main()
