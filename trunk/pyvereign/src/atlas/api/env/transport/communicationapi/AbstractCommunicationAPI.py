from atlas.api.env.transport.communicationapi.CommunicationAPIAdapter import CommunicationAPIAdapter

class AbstractCommunicationAPIAdapter(CommunicationAPIAdapter):
    
    def initialize(self):
        self._inetAddress = None
    
    def open(self, inetAddress):
        self._inetAddress = inetAddress