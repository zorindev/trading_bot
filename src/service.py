
import os
import asyncio
import tornado
import tornado.web
import tornado.options
import tornado.platform.asyncio
from tornado.options import define, options
import tornado.websocket

import logging
from logger import logger
logger.setLevel(logging.DEBUG)

from core import WSOnMessageHandler

from core.const import const as sv


# interprets message content
globalMessageHandler = None

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class StaticJSHandler(tornado.web.StaticFileHandler):
    def get_content_type(self):
        return 'application/javascript'

class WebSocketServer(tornado.websocket.WebSocketHandler):

    
    def check_origin(self, origin):
        return True

    def open(self):
        """
        opens a socket and instantiates components
        """

        # this object has to be global
        global globalMessageHandler

        logger.debug("opening socket connection")

        if(globalMessageHandler == None):
            logger.debug(" XXX 1 message handler object will be initialized")
            globalMessageHandler = (WSOnMessageHandler.WSOnMessageHandler()).getInstance()
            globalMessageHandler.initState({
                sv.CONFIG_WEBSOCKET: self,
                sv.CONFIG_ENCODER: tornado.escape
            })
        else:
            logger.debug(" XXX 2 message handler object has already been initialized")
            globalMessageHandler.refreshSocket(self)


    def on_close(self):
        """
        closes the socket
        """
        logger.info("closing socket")

    def on_message(self, message):
        """
        interprets message content
        """
        logger.info(" handling message ")
        globalMessageHandler.handleMessage(message)
       


class AppImpl(tornado.web.Application):

     def __init__(self):
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "web"),
            static_path = os.path.join(os.path.dirname(__file__), "web"),
            debug = True,
            autoreload = True
        )

        handlers = [
            (r"/", IndexHandler),
            (r"/websocket", WebSocketServer)
        ]

        super(AppImpl, self).__init__(handlers, **settings)


def main():
    logger.info("starting service ... ")

    define("port", default=8888, help="", type=int)
    asyncio.set_event_loop_policy(tornado.platform.asyncio.AnyThreadEventLoopPolicy())
    tornado.options.parse_command_line()
    app = AppImpl()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
    
    
if __name__ == "__main__":
    """
    entry
    """    
    main()