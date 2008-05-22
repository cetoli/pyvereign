from org.pyvereign.core.environment.service.AbstractTransportService import AbstractTransportService
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.transport.receiver.ReceiverFactory import ReceiverFactory
from org.pyvereign.core.environment.transport.address.BindIPv4Address import BindIPv4Address
from org.pyvereign.core.environment.transport.listener.StreamListener import StreamListener
from org.pyvereign.core.environment.transport.address.InetAddress import InetAddress
from org.pyvereign.core.environment.transport.forwarder.ForwarderFactory import ForwarderFactory
from org.pyvereign.core.exception.TransportError import TransportError
from org.pyvereign.core.environment.transport.listener.TransportListener import TransportListener
from org.pyvereign.core.exception.BindError import BindError
from org.pyvereign.core.exception.TransportServiceError import TransportServiceError
from org.pyvereign.core.microkernel.CoreServiceRequest import CoreServiceRequest
from org.pyvereign.core.microkernel.CoreServiceResponse import CoreServiceResponse
from org.pyvereign.core.microkernel.Microkernel import Microkernel


class DefaultTransportService(AbstractTransportService):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: version
    """
    
    def __init__(self):
        self.init()
        
    def initialize(self, owner, id, context):
        AbstractTransportService.initialize(self, owner, id, context)
        
        if not self._owner.hasModule(IDFactory().createCoreServiceID(self._owner, Constants.NETWORKING_SERVICE)):
            raise RuntimeError()
        
        service = self._owner.getModule(IDFactory().createCoreServiceID(self._owner, Constants.NETWORKING_SERVICE))
        
        protocols = service.getNetworkProtocols()
        
        for p in protocols:
            self._protocols[p.getName()] = p
            receiver = ReceiverFactory().createReceiver(p.getName(), BindIPv4Address(), p)
            listener = StreamListener(receiver)
            self._streamListeners[p.getName()] = listener
        
    def sendStream(self, protocolName, inetAddress, stream, broadcasting = False, timeout = 0):
        if not protocolName:
            raise RuntimeError("protocolName parameter is none.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName parameter is not an instance of str class.")
        if not inetAddress:
            raise RuntimeError("inetAddress parameter is none.")
        if not isinstance(inetAddress, InetAddress):
            raise TypeError("inetAddress parameter is not an instance of InetAddress class.")
        if not stream:
            raise RuntimeError("stream parameter is none.")
        if not isinstance(protocolName, str):
            raise TypeError("stream parameter is not an instance of str class.")
        if broadcasting == None:
            raise RuntimeError("broadcasting parameter is none.")
        if not isinstance(protocolName, str):
            raise TypeError("broadcasting parameter is not an instance of bool class.")
        
        forwarder = ForwarderFactory().createForwarder(protocolName, inetAddress, self._protocols[protocolName])
        try:
            try:
                forwarder.open()
                if inetAddress.isBroadcastAddress() and broadcasting == True:
                    forwarder.supportBroadcasting(broadcasting)
                if not inetAddress.isBroadcastAddress() and broadcasting == True:
                    raise TransportError("Invalid configuration for the broadcasting of stream.")
                if timeout > 0:
                    forwarder.setTimeout(timeout)
                elif timeout < 0:
                    raise TransportError("Invalid timeout value.")
                return forwarder.send(stream)
            except:
                raise
        finally:
            forwarder.close()
    
    def addTransportListener(self, protocolName, uri, listener):
        if not protocolName:
            raise RuntimeError("protocolName is none.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName is not an instance of str class.")
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        if not listener:
            raise RuntimeError("listener is none.")
        if not isinstance(listener, TransportListener):
            raise TypeError("listener is not an instance of TransportListener class.")
        streamListener = self._streamListeners[protocolName]
        return streamListener.addTransportListener(uri, listener)
    
    def removeTransportListener(self, protocolName, uri):
        if not protocolName:
            raise RuntimeError("protocolName is none.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName is not an instance of str class.")
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        streamListener = self._streamListeners[protocolName]
        return streamListener.removeTransportListener(uri)
    
    def getTransportListener(self, protocolName, uri):
        if not protocolName:
            raise RuntimeError("protocolName is none.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName is not an instance of str class.")
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        streamListener = self._streamListeners[protocolName]
        return streamListener.getTransportListener(uri)
    
    def start(self, params):
        print "Starting Transport Service ..."
        if len(params) > 0:
            try:
                for l in self._streamListeners.values():
                    l.open(params[0])
                    l.reuseAddress(True)
                    l.start()
            except (TransportError, BindError), e:
                raise TransportServiceError(e)
        AbstractTransportService.start(self, params)
        print "Done."
    
    def getNumberOfTransportListeners(self):
        number = 0
        for listeners in self._streamListeners.values():
            number += listeners.getNumberOfTransportListeners()
        return number

    def stop(self):
        if not self._status == DefaultTransportService.STARTED:
            raise TransportError("Service was not started.")
        try:
            for l in self._streamListeners.values():
                l.close()
            AbstractTransportService.stop(self)
        except:
            raise