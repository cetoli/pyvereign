from org.pyvereign.core.environment.transport.address.InetAddressFactory import InetAddressFactory
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.communication.endpoint.protocol.MessageSender import MessageSender
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
from org.pyvereign.core.communication.format.Format import Format
from org.pyvereign.core.microkernel.Microkernel import Microkernel

class AbstractMessageSender(MessageSender):
    """
    Defines the generic implementation of MessageSender interface.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def init(self, endpointAddress, format, kernel):
        if not isinstance(endpointAddress, EndpointAddress):
            raise TypeError()
        if not isinstance(format, Format):
            raise TypeError()
        if not isinstance(kernel, Microkernel):
            raise TypeError()
        self._endpointAddress = endpointAddress
        self._format = format
        self._kernel = kernel
        
    def sendMessage(self, message, timeout = 0):
        destination = message.getDestination()
        address = None
        if destination.getInetAddress().isBroadcastAddress():
            address = InetAddressFactory.createBroadcastAddress(destination.getPort())
        else:
            address = InetAddressFactory.createInetAddress(destination.getIPAddress(), destination.getPort())
        try:
            server = self._kernel.getModule(IDFactory().createInternalServerID(Constants.ENVIRONMENT))
            server.sendStream(self._endpointAddress.getProtocol(), address, self._format.marshal(message), address.isBroadcastAddress(), timeout)
            return message
        except:
            raise