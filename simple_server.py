"""
server.py

Websocket server
"""
import json

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'

    def on_message(self, message):
        message = json.loads(message)
        if message['command'] == 'get_colors':
            self.write_message('Red, Blue, Green')
        if message['command'] == 'get_shapes':
            self.write_message('Circle, Square, Triangle')

    def on_close(self):
      print 'connection closed'

application = tornado.web.Application([
    (r'/ws', WSHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
