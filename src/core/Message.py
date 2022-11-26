

import uuid
import logging
from datetime import datetime

from .const import const as ms


class Message(object):

    # instance
    instance = None
    
    # payload
    payload = None

    def __init__(self):
        """
        init
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.payload = {}
        self.logger.debug("initializing message ... ")


    def getInstance(self):
        """
        gets instance
        """
        self.logger.debug("getting message instance ... ")
        if(self.instance == None):
            self.instance = Message()
        return self.instance


    def resetMessage(self):
        """
        resets
        """

        self.logger.debug("resetting message ")
        self.payload = {
            "id":               str(uuid.uuid4()),
            "timestamp":        str(int(datetime.utcnow().timestamp())),
        }


    def getPayload(self):
        """
        get payload
        """
        return self.payload
