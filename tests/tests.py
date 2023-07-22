import unittest
from ioc_parser.utils import is_ip_address


class TestIPAddress(unittest.TestCase):
    def test_valid_ipv4_address(self):
        self.assertTrue(is_ip_address("192.168.1.1"))

    def test_valid_ipv6_address(self):
        self.assertTrue(is_ip_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))

    def test_invalid_ipv4_address(self):
        self.assertFalse(is_ip_address("256.256.256.256"))

    def test_invalid_ipv6_address(self):
        self.assertFalse(is_ip_address("invalid_ip_address"))


if __name__ == "__main__":
    unittest.main()
