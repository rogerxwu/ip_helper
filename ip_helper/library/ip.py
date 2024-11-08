from abc import ABC, abstractmethod


# abstract based class as the blueprint of the class IPV4 and IPV6
class IP(ABC):
    @abstractmethod
    def get_ip(self):
        pass

    @abstractmethod
    def get_ip_available(self):
        pass

    @abstractmethod
    def get_ip_usable(self):
        pass
