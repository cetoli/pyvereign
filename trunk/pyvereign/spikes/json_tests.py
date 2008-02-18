from atlas.api.com.endpoint.message.EndpointMessage import EndpointMessage
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
import json

message = EndpointMessage(EndpointAddress("TCP", "192.168.1.10", 5050), EndpointAddress("TCP", "192.168.1.8", 5050))

s = json.write(message.getValues())
print s