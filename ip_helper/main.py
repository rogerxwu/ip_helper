#!/usr/bin/env python3
""" 
IP Helper Tool: Provides detailed information about a given IP/subnet.

This script takes an IP address and subnet mask in CIDR format (e.g., 192.168.1.0/24)
as input and calculates subnet-related details such as network address, broadcast
address, usable IP range, and other relevant data.
"""
import logging
import argparse
from ip_helper.library.ipv4 import IPV4

# from ip_helper.library.ipv6 import IPV6
from ip_helper.library.ip_schema import IPAddressModel

# Configure logging for debugging and error tracking
logger = logging.getLogger(__name__)


def main():
    """
    Main function to parse input, validate it, and display subnet details.

    - Accepts a subnet in CIDR format via command-line arguments.
    - Validates the input format using a predefined schema.
    - Uses the IPV4 class to compute and display various subnet attributes.
    """
    parser = argparse.ArgumentParser(
        prog="IP Helper", description="Calculate subnet details"
    )
    parser.add_argument("subnet", type=str, help="Enter subnet in format IP/submask")
    args = parser.parse_args()
    valid_input = IPAddressModel(address=args.subnet)
    # Need validate the subnet argument format
    ip = str(valid_input.address.ip)
    submask = str(valid_input.address.network.prefixlen)

    ip = IPV4(ip=ip, submask_len=int(submask))
    print(f"IP Address: {ip.get_ip()}")
    print(f"Network Address: {ip.get_ip_network_address()}")
    print(f"Usable Host IP Range: {ip.get_ip_range()}")
    print(f"Broadcast Address: {ip.get_ip_broadcast_address()}")
    print(f"Total Number of Hosts: {ip.get_ip_available()}")
    print(f"Number of Usable Hosts {ip.get_ip_usable()}")
    print(f"Subnet Mask: {ip.get_submask_in_ip()}")
    print(f"Wildcard Mask: {ip.get_wildcard_mask_in_ip()}")
    print(f"Binary Subnet Mask: {ip.get_submask_in_binary()}")
    print(f"CIDR Notation: /{submask}")
    print(f"IP Type: {ip.get_ip_type()}")


if __name__ == "__main__":
    main()
