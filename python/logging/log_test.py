import logging
logger = logging.getLogger('spam_app')
logger.setLevel(logging.DEBUG)

fh =  logging.FileHandler('spam.log')
fh.setLevel(logging.INFO)

logger.addHandler(fh)

#logger.info('create the first info log')
logger.debug('create the first debug log')

