from org.pyvereign.environment.transport.address.abstract_inet_address import AbstractInetAddress

class DefaultInetAddress(AbstractInetAddress):
    
    def __init__(self, ipaddress, port, family):
        self.setFamily(family)
        self.setIPAddress(ipaddress)