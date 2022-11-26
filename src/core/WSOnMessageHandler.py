import os
import logging
import threading
import json

from .Transmission import Transmission
from .Engine import Engine

from .const import const as hn


# GLOBALS
message_queue = []
signal_queue = []


class WSOnMessageHandler(object):
    
    # congig
    config = None

    # instance
    instance = None

    # singleton of tr
    transmission = None

    # tr thread
    transmissionThread = None

    # singleton of en
    engine = None

    # en thread
    engineThread = None

    def __init__(self):
        """
        init
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)


    def getInstance(self):
        """
        return singleton instance
        """
        if(self.instance == None):
            self.instance = WSOnMessageHandler()
        return self.instance


    def initState(self, __config):
        """
        inits transmission and engine
        """

        global message_queue, signal_queue

        self.logger.debug("initializing state ... ")

        self.config = {
            hn.CONFIG_MESSAGE_QUEUE: message_queue,
            hn.CONFIG_SIGNAL_QUEUE: signal_queue
        }

        self.config = { **self.config, **__config }

        self.transmission = (Transmission()).getInstance()
        self.transmission.setConfig(self.config)
        self.transmissionThread = threading.Thread(target = self.transmission.run)

        self.engine = (Engine()).getInstance()
        self.engine.setConfig(self.config)
        self.engineThread = threading.Thread(target = self.engine.run)


    def refreshSocket(self, newSocket):
        """
        when UI reloads we need to supply the new socket connection
        """

        # TODO: this mechanism overwrites the socket to channel the messages to
        # instead all sockets should be tracked and messages should be broadcasted
        self.config[hn.CONFIG_WEBSOCKET] = newSocket
        if(self.transmission != None):
            self.transmission.setConfig(self.config)


    def handleMessage(self, message):
        """
        handles messages based on actions
        instantiates state components
        """

        self.logger.debug(" in message handler " + message)
        message = json.loads(message)
        action = message[hn.MSG_HNDL_CLNT_MESSAGE_VALUE]

        transmissionState = self.transmission.getState()
        engineState = self.engine.getState()

        self.logger.debug("transmission state: " + str(transmissionState))
        self.logger.debug("enging state: " + str(engineState))

        try:

            if(action == hn.MSG_HNDLR_ACTION_START):

                if(transmissionState == hn.TRANSMISSION_OFF):
                    self.logger.debug(" in start ")
                    try:
                        self.transmission.goIntoGear()
                        self.transmissionThread.start()
                    except RuntimeError:
                        self.transmissionThread = threading.Thread(target = self.transmission.run)
                        self.transmissionThread.start()
                else:
                    self.logger.debug("transmission is already running")


                if(engineState == hn.ENGINE_STATE_OFF):
                    try:
                        self.engine.start()
                        self.engineThread.start()
                    except RuntimeError:
                        self.engineThread = threading.Thread(target = self.engine.run)
                        self.engineThread.start()
                else:
                    self.logger.debug("engine is already running")

            elif(action == hn.MSG_HNDLR_ACTION_STOP):
                self.transmission.turnOff()
                self.engine.stop()
                self.transmissionThread.join()
                self.engineThread.join()

            elif(action == hn.MSG_HNDLR_ACTION_PAUSE):
                self.transmission.goIntoNeutral()

            elif(action == hn.MSG_HNDLR_ACTION_RESUME):
                self.transmission.goIntoGear()

            elif(action == hn.MSG_HNDLR_ACTION_STATUS):
                self.logger.debug(" STATUS was called ")


        except Exception as e:
            self.logger.error(e)
            self.logger.debug(" in exception handling in WSOnMessageHandler ")

    
