import unittest
from ioc_parser.parser import IOCParser
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


class TestProccessIOCs(unittest.TestCase):
    def test_process_iocs_empty_lines(self):
        content = """
http://spotifyvault.com/default/redirecttoken/394f6472-66ef-41a7-8019b56562578535
http://jcbuid23--memomendezrange.repl.co/
https://4567-87356.000webhostapp.com/applogin.html
https://apple.appleidjs.com/
https://metapay-zahlen.sbs/


"""

        expected = {
            "urls": [
                "http://spotifyvault.com/default/redirecttoken/394f6472-66ef-41a7-8019b56562578535",
                "http://jcbuid23--memomendezrange.repl.co/",
                "https://4567-87356.000webhostapp.com/applogin.html",
                "https://apple.appleidjs.com/",
                "https://metapay-zahlen.sbs/",
            ],
            "ip_addresses": [],
        }
        parser = IOCParser("fakesource", "", 0, None)
        processed_ioc = parser.process_content(content)

        self.assertEqual(processed_ioc, expected)

    def test_process_iocs_ip_address_and_urls(self):
        content = """1;https://apple.appleidjs.com/
2;https://metapay-zahlen.sbs/
3;192.0.0.1"""
        expected = {
            "urls": [
                "https://apple.appleidjs.com/",
                "https://metapay-zahlen.sbs/",
            ],
            "ip_addresses": ["192.0.0.1"],
        }

        parser = IOCParser("fakesource", ";", 1, None)
        processed_ioc = parser.process_content(content)

        self.assertEqual(processed_ioc, expected)


if __name__ == "__main__":
    unittest.main()
