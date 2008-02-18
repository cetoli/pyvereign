from atlas.api.com.endpoint.format.MessageFormat import MessageFormat
from json import WriteException
from atlas.api.exception.MessageFormatError import MessageFormatError
from json import ReadException
from atlas.api.com.endpoint.message.EndpointMessage import EndpointMessage
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
import json

class JSONMessageFormat(MessageFormat):
    
    def __init__(self):
        print ""
    
    def marshal(self, message):
        try:
            return json.write(message.getValues())
        except WriteException, e:
            raise MessageFormatError(e)
    
    def unmarshal(self, stream):
        try:
            values = json.read(stream)
            message = EndpointMessage(EndpointAddress.toEndpointAddress(values["origin"]), EndpointAddress.toEndpointAddress(values["destination"]))
            return message
        except ReadException, e:
            raise MessageFormatError(e)