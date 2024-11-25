#!/usr/bin/env python3
"""
This class implements methods for working with IPv4 addresses. It provides 
utilities for subnetting, address type determination, and binary/decimal conversions.
"""
from ip_helper.library.ip import IP


class IPV4(IP):
    """Class for handling IPv4-specific operations, derived from the abstract IP base class."""

    def __init__(self, ip: str, submask_len: int) -> None:
        """
        Initialize an IPv4 object.
        
        Args:
            ip (str): The IPv4 address in dotted-decimal notation (e.g., '192.168.1.1').
            submask_len (int): The subnet mask length (e.g., 24 for '/24').
        """
        self.length = 32
        self.ip = ip
        self.submask_len = submask_len

    def get_ip(self) -> str:
        """
        Retrieve the IPv4 address.
        
        Returns:
            str: The IPv4 address in dotted-decimal notation.
        """
        return self.ip

    def get_ip_available(self) -> int:
        """
        Calculate the total number of IP addresses in the subnet.
        
        Returns:
            int: The total number of IPs, including network and broadcast addresses.
        """
        return 2 ** (32 - int(self.submask_len))

    def get_ip_usable(self) -> int:
        """
        Calculate the number of usable IP addresses in the subnet.
        
        Returns:
            int: The number of usable IPs (excludes network and broadcast addresses).
            Returns 0 for /32, as no usable addresses exist in that case.
        """
        # Corner case is when submask len is 32, no negative will return
        return 0 if self.submask_len == 32 else (2 ** (32 - int(self.submask_len)) - 2)

    def get_submask_in_ip(self) -> str:
        """
        Generate the subnet mask in dotted-decimal format.
        
        Converts the subnet length into a binary string and formats it as an IPv4 address.
        
        Returns:
            str: The subnet mask (e.g., '255.255.255.0' for /24).
        """
        submask_in_binary = "1" * self.submask_len + "0" * (
            self.length - self.submask_len
        )
        first_octlet = int(submask_in_binary[0:8], 2)
        second_octlet = int(submask_in_binary[8:16], 2)
        third_octlet = int(submask_in_binary[16:24], 2)
        fourth_octlet = int(submask_in_binary[24:32], 2)
        return f"{first_octlet}.{second_octlet}.{third_octlet}.{fourth_octlet}"

    def get_submask_in_binary(self) -> str:
        """
        Retrieve the subnet mask in binary format.
        
        Returns:
            str: Binary representation of the subnet mask 
                (e.g., '11111111.11111111.11111111.00000000').
        """
        return self.convert_ip_to_binary(self.get_submask_in_ip())

    def get_wildcard_mask_in_ip(self) -> str:
        """
        Generate the wildcard mask in dotted-decimal format.
        
        The wildcard mask is the inverse of the subnet mask, used in access control and routing.
        
        Returns:
            str: The wildcard mask (e.g., '0.0.0.255' for /24).
        """
        submask_in_binary = "0" * self.submask_len + "1" * (
            self.length - self.submask_len
        )
        first_octlet = int(submask_in_binary[0:8], 2)
        second_octlet = int(submask_in_binary[8:16], 2)
        third_octlet = int(submask_in_binary[16:24], 2)
        fourth_octlet = int(submask_in_binary[24:32], 2)
        return f"{first_octlet}.{second_octlet}.{third_octlet}.{fourth_octlet}"

    def convert_ip_to_binary(self, ip_in_int: str) -> str:
        """
        Convert an IPv4 address from dotted-decimal to binary format.
        
        Args:
            ip_in_int (str): IPv4 address in dotted-decimal format.
        
        Returns:
            str: Binary representation of the IPv4 address.
        """
        ip_divided_by_octlet = ip_in_int.split(".")
        output = []
        for octlet in ip_divided_by_octlet:
            all_zero_octlet = ["0"] * 8
            octlet_in_binary = str(bin(int(octlet))[2:])
            for i, v in enumerate(octlet_in_binary):
                if v == "1":
                    all_zero_octlet[8 - len(octlet_in_binary) + i] = "1"
            output.append("".join(all_zero_octlet))

        return ".".join(output)

    def convert_binary_to_ip(self, ip_in_binary: str) -> str:
        """
        Convert an IPv4 address from binary to dotted-decimal format.
        
        Args:
            ip_in_binary (str): Binary representation of an IPv4 address.
        
        Returns:
            str: IPv4 address in dotted-decimal format.
        """
        ip_divided_by_octlet = ip_in_binary.split(".")
        output = []
        for octlet in ip_divided_by_octlet:
            octlet_in_int = int(octlet, 2)
            output.append(str(octlet_in_int))
        return ".".join(output)

    def get_ip_network_address(self) -> str:
        """
        Do bitwise AND operation on ip and submask to get the network address of the subnet.
        
        Args:
            ip_in_binary (str): Binary representation of IPv4 address.
        Returns:
            str: IPv4 network address in dotted-decimal format
        """
        ip_divided_by_octlet = self.convert_ip_to_binary(self.ip).split(".")
        submask_divided_by_octlet = self.convert_ip_to_binary(
            self.get_submask_in_ip()
        ).split(".")
        output = []
        for i in range(4):
            bitwise_and = int(ip_divided_by_octlet[i], 2) & int(
                submask_divided_by_octlet[i], 2
            )
            output.append(str(bitwise_and))
        return ".".join(output)

    def get_ip_broadcast_address(self) -> str:
        """
        Calculate the broadcast address of the subnet.

        The broadcast address is obtained by performing a bitwise OR operation 
        between the IP address and the wildcard mask. It is the highest address 
        in the subnet and is used to send packets to all devices within the subnet.

        Returns:
            str: The broadcast address in dotted-decimal format.
        """
        ip_divided_by_octlet = self.convert_ip_to_binary(self.ip).split(".")
        submask_divided_by_octlet = self.convert_ip_to_binary(
            self.get_wildcard_mask_in_ip()
        ).split(".")
        # print(ip_divided_by_octlet) # uncomment for debugging
        # print(submask_divided_by_octlet) # uncomment for debugging
        output = []
        for i in range(4):
            bitwise_and = int(ip_divided_by_octlet[i], 2) | int(
                submask_divided_by_octlet[i], 2
            )
            output.append(str(bitwise_and))
        return ".".join(output)

    def get_ip_range(self) -> str:
        """
        Calculate the range of usable IP addresses in the subnet.

        The usable IP range excludes the network address and broadcast address.
        Special cases:
        - For subnets with /31 or /32, no usable IP addresses exist.

        Returns:
            str: A string representing the range of usable IPs in the format 
                'first_ip ~ last_ip', or 'NA' if no usable IPs exist.
        """
        # Corner case, when submask length is 31 or 32, no usable IP
        if self.submask_len == (31, 32):
            return "NA"
        # first ip is the network address + 1
        ip_divided_by_octlet = self.get_ip_network_address().split(".")
        ip_divided_by_octlet[3] = str(int(ip_divided_by_octlet[3]) + 1)
        first_ip = ".".join(ip_divided_by_octlet)
        # last ip is the broadcast address - 1
        ip_divided_by_octlet = self.get_ip_broadcast_address().split(".")
        ip_divided_by_octlet[3] = str(int(ip_divided_by_octlet[3]) - 1)
        last_ip = ".".join(ip_divided_by_octlet)
        return f"{first_ip} ~ {last_ip}"

    def get_ip_type(self) -> str:
        """
        Determine whether the IP address is public or private.

        Private IP ranges:
        - 10.0.0.0 to 10.255.255.255 (/8)
        - 172.16.0.0 to 172.31.255.255 (/12)
        - 192.168.0.0 to 192.168.255.255 (/16)

        Returns:
            str: 'Private' if the IP belongs to a private range, otherwise 'Public'.
        """
        return (
            "Private"
            if self.check_if_ip_in_subnet(self.ip, "10.0.0.0/8")
            or self.check_if_ip_in_subnet(self.ip, "172.16.0.0/12")
            or self.check_if_ip_in_subnet(self.ip, "192.168.0.0/16")
            else "Public"
        )

    def check_if_ip_in_subnet(self, ip, subnet) -> bool:
        """
        Check if the given IP address belongs to the specified subnet.

        Compares the binary representations of the network addresses for both
        the IP and the subnet, using the subnet mask length to determine equality.

        Args:
            ip (str): The IP address to check (e.g., '192.168.1.10').
            subnet (str): The subnet in CIDR format (e.g., '192.168.1.0/24').

        Returns:
            bool: True if the IP address is within the subnet, False otherwise.
        """
        subnet_ip = subnet.split("/")[0]
        subnet_submask = int(subnet.split("/")[1])
        ip_network_address_in_binary = self.convert_ip_to_binary(ip).replace(".", "")[
            0:subnet_submask
        ]
        subnet_network_address_in_binary = self.convert_ip_to_binary(subnet_ip).replace(
            ".", ""
        )[0:subnet_submask]

        return ip_network_address_in_binary == subnet_network_address_in_binary
