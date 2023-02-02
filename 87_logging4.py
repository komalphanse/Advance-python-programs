import logging
logging.basicConfig(filename='newfile.log',filemode='w',format='%(asctime)s-%(message)s')
logger=logging.getLogger()#creating an object of the logging
logger.setLevel(logging.DEBUG)#test message
logger.debug("This is a harmless debug message")
logger.info("This is just an infomration")
logger.error("you are trying to divide by zero")
logger.critical("internet s down")
