import unittest
from ip_helper.library.ipv4 import IPV4


class TestIPHelper(unittest.TestCase):
    def test_valid_subnet(self):
        ip = IPV4(ip="192.168.0.1", submask_len=24)
        self.assertEqual(ip.get_ip(), "192.168.0.1")
        self.assertEqual(ip.get_ip_network_address(), "192.168.0.0")
        self.assertEqual(ip.get_ip_broadcast_address(), "192.168.0.255")

    def test_invalid_ip(self):
        with self.assertRaises(ValueError):
            IPV4(ip="192.168.0.1", submask_len="35")


if __name__ == "__main__":
    unittest.main()
