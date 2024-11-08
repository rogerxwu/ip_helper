#!/usr/bin/env python3
""" 
This abstract based class serves as the blueprint of the class IPV4 and IPV6
"""
from abc import ABC, abstractmethod


class IP(ABC):
    """Abstrack class IP"""

    @abstractmethod
    def get_ip(self):
        """abstract function"""
        raise NotImplementedError("Subclass must implement this method")

    @abstractmethod
    def get_ip_available(self):
        """abstract function"""
        raise NotImplementedError("Subclass must implement this method")

    @abstractmethod
    def get_ip_usable(self):
        """abstract function"""
        raise NotImplementedError("Subclass must implement this method")
