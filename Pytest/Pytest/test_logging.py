import logging

def test_logging():

    logger = logging.getLogger(__name__)  # will capture test name

    fileHandler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s") # in wich format the data will be printed

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #file handler we set up how the log report should work

    logger.setLevel(logging.DEBUG)

    logger.debug('A debug method is executed')

    logger.info('Information statement')

    logger.warning('Not critical issue occured')

    logger.error('Critical issue occured')

    logger.critical("Critical issue")

