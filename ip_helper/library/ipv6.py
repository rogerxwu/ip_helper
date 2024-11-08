#!/usr/bin/env python3
""" 
This derived class from abstract base class IP provides methods for IPV6
"""
from ip_helper.library.ip import IP


class IPV6(IP):
    """Derived class IPV6 from abstract base class IP"""

    def __init__(self) -> None:
        """Constructor"""
        # length = 128
