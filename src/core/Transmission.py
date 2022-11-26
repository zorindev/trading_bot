
import sys
import logging
import time

from .const import const as tr



class Transmission(object):

    # singleton
    instance = None

    # ws handler to send messages
    webSocket = None

    # json encoder
    endoder = None

    # run flag
    gear = None    

    # global message queue
    message_queue = None

    # global signal queue
    signal_queue = None


    def __init__(self):
        """
        init
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.gear = tr.TRANSMISSION_OFF

        self.logger.debug("initializing transmission ... ")


    def getInstance(self):
        """
        return singleton instance
        """
        self.logger.debug("getting transmissions instance ... ")
        if(self.instance == None):
            self.instance = Transmission()
        return self.instance


    def setConfig(self, config):
        """
        sets config of the object
        """
        self.logger.debug("initializing transmission's config ...")
        self.webSocket = config[tr.CONFIG_WEBSOCKET]
        self.encoder = config[tr.CONFIG_ENCODER]
        self.message_queue = config[tr.CONFIG_MESSAGE_QUEUE]
        self.signal_queue = config[tr.CONFIG_SIGNAL_QUEUE]

    
    def goIntoGear(self):
        """
        engage
        """
        self.gear = tr.TRANSMISSION_GEAR


    def goIntoNeutral(self):
        """
        disengage
        """
        self.gear = tr.TRANSMISSION_NEUTRAL


    def turnOff(self):
        """
        turn off transmission
        """
        self.gear = tr.TRANSMISSION_OFF


    def getState(self):
        """
        gets state
        """
        return self.gear


    def run(self):
        """
        holds the main loop that dispatches the messages
        """
        self.logger.debug(" in the transmissions RUN method ")

        while(not (self.gear == tr.TRANSMISSION_OFF)):

            if(self.gear == tr.TRANSMISSION_GEAR):

                try:
                    message = self.message_queue.pop(0)
                    self.webSocket.write_message(self.encoder.json_encode(message))
                except Exception as e:
                    self.logger.debug(e)

            time.sleep(tr.TRANMISSION_FREQUENCEY)




