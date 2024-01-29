import inspect
import logging

class logclass:
    
    def __init__(self, driver):
        self.driver = driver

    def customLogger(logLevel=logging.DEBUG):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.DEBUG)
        fileHandler = logging.FileHandler("Logs/logfile.log", mode='a')
        fileHandler.setLevel(logLevel)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger
