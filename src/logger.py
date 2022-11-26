
import sys
import logging
from logging.handlers import RotatingFileHandler

logger = None
try:
    #logging.basicConfig(level=logging.DEBUG)
    logging.root.setLevel(logging.DEBUG)
    logging.getLogger('root').setLevel(logging.DEBUG)
    logger = logging.getLogger("trading")


    file_handler = RotatingFileHandler('./logs/' + (__name__) + '.log', maxBytes=200000, backupCount=10)
    file_handler.setLevel(logging.DEBUG)

    std_handler = logging.StreamHandler(sys.stdout)
    std_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    std_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(std_handler)

except Exception as excp:
    logging.basicConfig(level=logging.DEBUG)
    logging.root.setLevel(logging.DEBUG)
    logging.getLogger('root').setLevel(logging.DEBUG)
    logger = logging.getLogger("trading")

