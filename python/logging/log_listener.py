import logging
import logging.config
import time
import os

logging.config.fileConfig('logging.config')

t = logging.config.listen(9999)
t.start()

logger = logging.getLogger('simpleExample')
try:
    while True:
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error mesage')
        logger.critical('critical message')
        time.sleep(5)
except KeyboardInterrupt:
    logging.config.stopListening()
    t.join()
