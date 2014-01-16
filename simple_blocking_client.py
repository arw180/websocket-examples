"""
client.py

This example shows how easy it is to create a client WebSocket connection
in Python using a synchronous (i.e. blocking) architecture
"""
import json
from websocket import create_connection

ws = create_connection("ws://localhost:8888/ws")

data = {'command': 'get_colors'}
ws.send(json.dumps(data))
result =  ws.recv()
print "Received colors: '%s'" % result

data = {'command': 'get_shapes'}
ws.send(json.dumps(data))
result =  ws.recv()
print "Received shapes: '%s'" % result

ws.close()
