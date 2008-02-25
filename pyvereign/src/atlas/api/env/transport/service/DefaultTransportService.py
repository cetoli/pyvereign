from atlas.api.env.transport.service.AbstractTransportService import AbstractTransportService
from atlas.api.env.transport.forwarder.ForwarderFactory import ForwarderFactory
from atlas.api.env.transport.address.InetAddress import InetAddress
from atlas.api.env.transport.receiver.ReceiverFactory import ReceiverFactory
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.env.transport.listener.StreamListener import StreamListener
from sets import ImmutableSet
from atlas.api.exception.TransportServiceError import TransportServiceError
from atlas.api.exception.TransportError import TransportError
from atlas.api.exception.BindError import BindError
from atlas.api.env.transport.listener.TransportListener import TransportListener

class DefaultTransportService(AbstractTransportService):
    
    def __init__(self):
        self._status = DefaultTransportService.NON_INITIALIZED
        
    def initialize(self, environment):
        
        AbstractTransportService.initialize(self, environment)
        protocols = self._environment.executeService("protocol", "getProtocols")
        
        self._protocols = {}
        
        self._streamListeners = {}
        
        for p in protocols:
            self._protocols[p.getName()] = p
            receiver = ReceiverFactory().createReceiver(p.getName(), BindIPv4Address(), p)
            listener = StreamListener(self._environment, receiver)
            self._streamListeners[p.getName()] = listener
    
    def addTransportListener(self, protocolName,uri, listener):
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
    
    def start(self, *params):
        if (self._status == DefaultTransportService.INITIALIZED): 
            if len(params) > 0:
                try:
                    for l in self._streamListeners.values():
                        l.open(params[0])
                        l.reuseAddress(True)
                        l.start()
                    AbstractTransportService.start(self, *params)
                except (TransportError, BindError), e:
                    raise TransportServiceError(e)
        elif (self._status < DefaultTransportService.INITIALIZED):
            raise TransportServiceError("Service was not initialized.")
        elif (self._status == DefaultTransportService.STARTED):
            raise TransportServiceError("Service is already started.")
        
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
            
    def getProtocols(self):
        return ImmutableSet(self._protocols.values())

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
