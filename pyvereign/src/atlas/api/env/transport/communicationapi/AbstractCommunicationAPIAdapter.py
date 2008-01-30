from atlas.api.env.transport.communicationapi.CommunicationAPIAdapter import CommunicationAPIAdapter

class AbstractCommunicationAPIAdapter(CommunicationAPIAdapter):
    
    def initialize(self):
        self._inetAddress = None
    
    def getInetAddress(self):
        return self._inetAddress
