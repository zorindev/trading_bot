
import logging
import time

from .const import const as en
from .Message import Message


class Engine(object):

    # logger
    logger = None

    # instance
    instance = None

    # message queue
    message_queue = None

    # signal queue
    signal_queue = None

    # state
    state = None

    # message
    message = None

    def __init__(self) -> None:
        """
        init
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.state = en.ENGINE_STATE_OFF
        self.message = (Message()).getInstance()
        self.logger.debug("initializing engine ... ")


    def getInstance(self):
        """
        gets the instance
        """

        self.logger.debug("getting engine instance ... ")
        if(self.instance == None):
            self.instance = Engine()
        return self.instance


    def setConfig(self, config):
        """
        sets config
        """

        self.message_queue = config[en.CONFIG_MESSAGE_QUEUE]
        self.signal_queue = config[en.CONFIG_SIGNAL_QUEUE]


    def start(self):
        """
        starts
        """
        self.state = en.ENGINE_STATE_SEARCHING


    def stop(self):
        """
        stops
        """
        self.state = en.ENGINE_STATE_OFF

    
    def pause(self):
        """
        pasuse
        """
        self.state = en.ENGINE_STATE_PAUSE

    def getState(self):
        """
        get state
        """
        return self.state


    def run(self):
        """
        engine loop
        """

        self.logger.debug(" in engine RUN method ")
        while(not (self.state == en.ENGINE_STATE_OFF)):
            if(self.state == en.ENGINE_STATE_SEARCHING):
                self.message.resetMessage()
                self.queueMessage()
            time.sleep(en.ENGINE_FREQUENCY)


    def queueMessage(self):
        """
        queues message into the queue
        """

        self.logger.debug("clearing message queue ...")
        try:
            for m in self.message_queue:
                self.message_queue.pop()
                del m
        except:
            pass

        self.logger.debug(" queing next message ... ")
        self.message_queue.append(self.message.getPayload())

