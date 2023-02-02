import logging
#create a custom logger_obj
logger_obj=logging.getLogger(__name__)
#create Handlers
w_handler=logging.StreamHandler()
e_handler=logging.FileHandler('file.log')
w_handler.setLevel(logging.WARNING)
e_handler.setLevel(logging.ERROR)
#create formatters and it to handlers
c_format=logging.Formatter("%(name)s-%(levelname)s-%(message)s")
f_format=logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
w_handler.setFormatter(c_format)
e_handler.setFormatter(f_format)
logger_obj.addHandler(w_handler)
logger_obj.addHandler(e_handler)
logger_obj.warning('tis is warning message')
logger_obj.error('this is error message')