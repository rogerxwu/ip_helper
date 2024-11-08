#! bin/usr/python
""" This module provides test """
#import pytest
from ip_helper.library.ipv4 import IPV4


def test_valid_subnet():
    """ Test valid subnet """
    ip = IPV4(ip="192.168.1.10", submask_len=24)
    assert ip.get_ip() == "192.168.1.10"
    assert ip.get_ip_network_address() == "192.168.1.0"
    assert ip.get_ip_broadcast_address() == "192.168.1.255"
    assert ip.get_ip_usable() == 254  # Usable hosts in /24
    assert ip.get_submask_in_ip() == "255.255.255.0"


# def test_invalid_submask_length():
#    with pytest.raises(
#        ValueError
#    ):  # Assuming IPV4 raises ValueError for invalid submask
#        IPV4(ip="192.168.1.10", submask_len=35)
