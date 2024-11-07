from abc import ABC, abstractmethod

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


