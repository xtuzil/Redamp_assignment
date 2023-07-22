import re


def is_ip_address(ioc: str) -> bool:
    """
    Check if ioc is an IP address using regex
    """

    # regex for ipv4 and ipv6
    ip_pattern = r"^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$|^(?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$"

    return re.match(ip_pattern, ioc) is not None


def strip_ioc(ioc: str) -> str:
    """
    Strip ioc from quotes
    """
    return ioc.strip('"').strip()
